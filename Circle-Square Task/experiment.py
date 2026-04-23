import expyriment
import random

expyriment.control.set_develop_mode(True)

#Initialization

exp = expyriment.design.Experiment(name="Circle-Square Task")
expyriment.control.initialize(exp)

#Subject info

subject_id = expyriment.io.TextInput("Subject ID (e.g. 01):").get()
group = expyriment.io.TextInput("Group (Patient / Control):").get()

#Constants

LATERAL_OFFSET  = 200
SHAPE_SIZE      = 50
N_TRIALS        = 20
RESPONSE_WINDOW = 2000  
ITI             = 500     
FIXATION_DURATION = 1000

KEY_LEFT  = expyriment.misc.constants.K_LEFT
KEY_RIGHT = expyriment.misc.constants.K_RIGHT

#Stimuli

fixation = expyriment.stimuli.FixCross(size=(30, 30), colour=(255, 255, 255))
fixation.preload()

blank = expyriment.stimuli.BlankScreen()
blank.preload()

circle = expyriment.stimuli.Circle(
    radius=SHAPE_SIZE // 2,
    colour=(255, 255, 255)
)

square = expyriment.stimuli.Rectangle(
    size=(SHAPE_SIZE, SHAPE_SIZE),
    colour=(255, 255, 255)
)

def set_configuration(config):
    if config == "A":
        circle.reposition((-LATERAL_OFFSET, 0))
        square.reposition(( LATERAL_OFFSET, 0))
        return "left"
    else:
        circle.reposition(( LATERAL_OFFSET, 0))
        square.reposition((-LATERAL_OFFSET, 0))
        return "right"

def present_stimuli():
    canvas = expyriment.stimuli.Canvas(
        size=exp.screen.size,
        colour=(0, 0, 0)
    )
    circle.plot(canvas)
    square.plot(canvas)
    canvas.present()

def run_trial(block_name, block_number, trial_number, circle_position):
    #Fixation
    fixation.present()
    exp.clock.wait(FIXATION_DURATION)

    #Stimuli + response
    present_stimuli()
    key, rt = exp.keyboard.wait(
        keys=[KEY_LEFT, KEY_RIGHT],
        duration=RESPONSE_WINDOW
    )

    blank.present()
    exp.clock.wait(ITI)

    if key is None or rt is None:
        validity  = "invalid"
        response  = "NA"
        rt_out    = "NA"
        correct   = "NA"
    else:
        validity = "valid"
        rt_out   = rt

        response = "left" if key == KEY_LEFT else "right"

        correct = "Correct" if response == circle_position else "Incorrect"

    return {
        "subject_id": "Sub-" + subject_id,
        "group":            group,
        "block":            block_number,
        "trial":            trial_number,
        "condition":        block_name,
        "circle_position":  circle_position,
        "response":         response,
        "validity":         validity,
        "correct":          correct,
        "rt":               rt_out,
    }


expyriment.control.start()

#Data file

exp.data.add_variable_names([
    "subject_id",
    "group",
    "block",
    "trial",
    "condition",
    "circle_position",
    "response",
    "validity",
    "correct",
    "rt",
])

#Block 1: Deterministic 
instructions_det = expyriment.stimuli.TextScreen(
    heading="Block 1: Press the arrow key matching the circle's side.",
    text="Press any key to begin.",
    heading_size=24,
    text_size=20,
    text_colour=(255, 255, 255),
    background_colour=(0, 0, 0),
)
instructions_det.present()
exp.keyboard.wait()

for t in range(1, N_TRIALS + 1):
    circle_pos = set_configuration("B")
    trial_data = run_trial(
        block_name="deterministic",
        block_number=1,
        trial_number=t,
        circle_position=circle_pos,
    )
    exp.data.add([
        trial_data["subject_id"],
        trial_data["group"],
        trial_data["block"],
        trial_data["trial"],
        trial_data["condition"],
        trial_data["circle_position"],
        trial_data["response"],
        trial_data["validity"],
        trial_data["correct"],
        trial_data["rt"],
    ])

#Block 2: Stochastic

instructions_sto = expyriment.stimuli.TextScreen(
    heading="Block 2: Press the arrow key matching the circle's side.",
    text="Press any key to begin.",
    heading_size=24,
    text_size=20,
    text_colour=(255, 255, 255),
    background_colour=(0, 0, 0),
)
instructions_sto.present()
exp.keyboard.wait()

#shuffled list of circle positions
half = N_TRIALS // 2
circle_positions = ["left"] * half + ["right"] * half
random.shuffle(circle_positions)

for t, pos in enumerate(circle_positions, start=1):
    config = "A" if pos == "left" else "B"
    circle_pos = set_configuration(config)
    trial_data = run_trial(
        block_name="stochastic",
        block_number=2,
        trial_number=t,
        circle_position=circle_pos,
    )
    exp.data.add([
        trial_data["subject_id"],
        trial_data["group"],
        trial_data["block"],
        trial_data["trial"],
        trial_data["condition"],
        trial_data["circle_position"],
        trial_data["response"],
        trial_data["validity"],
        trial_data["correct"],
        trial_data["rt"],
    ])

goodbye = expyriment.stimuli.TextScreen(
    heading="The experiment is complete.",
    text="Thank you!",
    heading_size=24,
    text_size=20,
    text_colour=(255, 255, 255),
    background_colour=(0, 0, 0),
)
goodbye.present()
exp.keyboard.wait()

expyriment.control.end()
