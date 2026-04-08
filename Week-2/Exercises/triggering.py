 


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

speed_1 = 5  
speed_2 = 20    
##issue with code, no collision

frames = 80   

#frame by frame advancement for each square


for i in range(frames): 
    red_square.move((speed_2, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(5)



for i in range(frames):
    green_square.move((speed_1, 0))
    red_square.present(clear=True, update=False)
    green_square.present(clear=False, update=True)
    exp.clock.wait(5)

red_square.present(clear=True, update=False)
green_square.present(clear=False, update=True)
exp.clock.wait(1000)

control.end()