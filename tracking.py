import numpy as np

# Defines a class to receive the characteristics of each line detection
class Line():
    def __init__(self):
        #polynomial coefficients averaged over the last n iterations
        self.best_fitA = []
        self.best_fitB = []
        self.best_fitC = []
        #polynomial coefficients for the most recent fit
        self.current_fit = [np.array([False])]  
        