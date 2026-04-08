 # Import the main modules of expyriment
from expyriment import design, control, stimuli

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

control.set_develop_mode()
# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)



square1 = stimuli.Rectangle(size=(50, 50), colour=[250, 0, 0], position=[-200, 0])
square2 = stimuli.Rectangle(size=(50, 50), colour=[0, 250, 0], position=[200, 0])

# Start running the experiment
control.start(subject_id=1)

square1.present(clear=True, update=False)
square2.present(clear=False, update=True)



# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()