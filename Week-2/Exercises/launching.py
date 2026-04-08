 


from expyriment import design, control, stimuli

exp = design.Experiment(name="Launching")

control.set_develop_mode(True)

control.initialize(exp)

red_square = stimuli.Rectangle(size=(50, 50), colour=[250, 0, 0], position=[-400, 0])

green_square = stimuli.Rectangle(size=(50, 50), colour=[0, 250, 0], position=[0, 0])

control.start(subject_id=1)

red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)
square_length=50

# Distance to travel = Initial distance between objects
displacement_x = 400
# Set speed
step_size = 10 # pixels per update
# Move left square until collision
while green_square.position[0] - red_square.position[0] < square_length:
    red_square.move((step_size, 0)) # (move-x, move-y)
red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)

# Move right square the same amount
while green_square.position[0] < displacement_x:
    green_square.move((step_size, 0)) 


red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

control.end()
