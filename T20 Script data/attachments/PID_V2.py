import numpy as np
import matplotlib.pyplot as plt
import mrcfile
import pandas as pd
from scipy import optimize

'''
This is the PID controller for the T20. Copied part of the code from the jupyter notebook
and converted it into a script for the Spectra. Will leave notes along the way so 
that anyone can continue and understand the code.
'''

class PID_Controller:

    def __init__(self, Kp_X, Ki_X, Kd_X, Kp_Y, Ki_Y, Kd_Y,T_c, T, measurement):
        self.Kp_X = Kp_X #Probability constant
        self.Ki_X = Ki_X #Integral Contstant
        self.Kd_X = Kd_X #Derivative Cosntant
        self.Kp_Y = Kp_Y
        self.Ki_Y = Ki_Y
        self.Kd_Y = Kd_Y
        self.setpoint = 0 #This should be the setpoint at which we want the position to stay at
        self.T_c = T_c #The time constant for derivative filtering 
        self.T = T #Time step, since it is even angle spacing, we can probs set it to 1
        self.measurement = measurement

        def Step(self, X_setpoint, Y_setpoint):
            ''' This is a single step of the controller. Will have to place this through a loop'''

            X_error = self.X_setpoint - self.measurement[1,:] #The error in the X_axis
            Y_error = self.Y_setpoint - self.measurment[0,:] #The error in the Y_axis

            Prob_X = self.Kp_X * X_error #Corresponding error for X
            Prob_Y = self.Kp_Y * Y_error #Corresponding error for Y

            self.integral_X += self.Ki_X * np.cumsum(Prob_X) * self.T
            self.integral_Y += self.Ki_Y * np.cumsum(Prob_Y) * self.T

            self.D_x = self.Kd_X * np.diff(Prob_X, prepend=0)
            self.D_y = self.Kd_Y * np.diff(Prob_Y, prepend=0)

        







