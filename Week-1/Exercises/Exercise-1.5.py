from quiz import *
import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))


run_quiz_from_csv("snippets.csv", section = "Dictionaries")