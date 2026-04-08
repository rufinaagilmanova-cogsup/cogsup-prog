###désespoir total 

# Import the main modules of expyriment
from expyriment import design, control, stimuli
from expyriment.misc import geometry

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

control.set_develop_mode()
# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)


triangle = stimuli.Shape(position=[-200, 0], vertex_list=geometry.vertices_triangle(50, 50, 50), colour=[150, 0, 150])
hexagon = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(n_edges=5, length=50), colour=[250, 250, 0], position=[200, 0])
t_label = stimuli.Line(start_point=[-200, 50], end_point=[-200, 100], line_width=3, colour=[250, 250, 250])

# Start running the experiment
control.start(subject_id=1)

triangle.present(clear=True, update=False)
hexagon.present(clear=False, update=True)
#t_label.present(clear=False, update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()