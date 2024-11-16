import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp
from scipy import optimize
from scipy.stats import norm


class PlotFunctions:

    def __init__(self, InsideSensor, OutsideSensor):
        self.InsideSensor = InsideSensor
        self.OutsideSensor = OutsideSensor


    def HistPlotFuncNorm(self, string, title, bins):
        fig, ax = plt.subplots(1,2, figsize = (11,5))
        #Plotting the histograms
        ax[0].hist(self.InsideSensor[string], bins = bins, color = 'red', label= 'Inside ' + string, edgecolor = 'black', density=True)
        ax[1].hist(self.OutsideSensor[string], bins = bins, color= 'blue', label= 'Outside ' +string, edgecolor= 'black', density= True)

        InMean, InStd = norm.fit(self.InsideSensor[string])
        OutMean, OutStd = norm.fit(self.OutsideSensor[string])

        xmin, xmax = ax[0].get_xlim()
        x = np.linspace(xmin, xmax, 100)

        ax[0].plot(x, norm.pdf(x, InMean, InStd), 'black', label= 'Inside Gaussian Fit')
        ax[1].plot(x, norm.pdf(x, OutMean, OutStd), 'black', label= 'Outside Gaussian Fit')
        #Setting Labels for the legends
        for i in range(len(ax)):
            ax[i].set(xlabel= string, ylabe = 'Density', title = title)
            ax[i].legend()

        print(f'The average {string} for the Inside and Outside Sensors are {InMean:.2f} (mb) and {OutMean:.2f} (mb)')



