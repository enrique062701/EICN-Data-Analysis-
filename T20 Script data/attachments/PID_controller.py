import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize

class PID_controller:

    def __init__(self, Kp, Ki, Kd, setpoint, data):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.data = data

    def PID_algorithm(self):
        #First is to get e  for each data point
        e_x = self.data[1,:] - self.setpoint
        e_y = self.data[0,:] - self.setpoint

        #Next is too start writing the functions
        P_x = self.Kp * e_x
        P_y = self.Kp * e_y
        #Note must make the integral to integrate before each step in order to predict the next step
        I_x = 0
        I_y = 0
        I_x += self.Ki * np.cumsum(e_x)#Every time it passes through the loop it takes the integral of the previous sum
        I_y += self.Ki * np.cumsum(e_y)

        D_x = self.Kd * np.diff(e_x, prepend=0)
        D_y = self.Kd * np.diff(e_y, prepend=0)

        #Now adding the whole thing together

        Measurement_x = self.data[1,:] - P_x + I_x + D_x
        Measurement_y = self.data[0,:] - P_y + I_y + D_y

        return Measurement_x, Measurement_y


    def update(self):




        




