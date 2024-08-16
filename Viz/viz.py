import matplotlib.pyplot as plt
import numpy as np

from time import time_ns, sleep

        
toSec = 1e9

# --- Class ------------------------------------------------------------------------------
class ShiftingGraph:
    def __init__(self, N_samples=100):
        """ 
        Arguments:
          N_samples: Amount of past samples visualized in graph
        """
        plt.ion()
        
        self.x = np.linspace(0, N_samples)
        self.y = np.zeros_like(self.x)

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_ylim(0,400)
        self.ax.set_ylabel("Measured distance (mm)")
        self.ax.set_xlabel("sample")
        self.line, = self.ax.plot(self.x, self.y, 'r-') # Returns a tuple of line objects, thus the comma


    def updateViz(self, y_new): 
        # update y-value array (pop & insert new value for right shifting effect)  
        self.y = np.insert(self.y[:-1], 0, y_new)
        
        # Update plot
        self.line.set_ydata(self.y)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


# --- Test Code ------------------------------------------------------------------------------
if __name__ == '__main__':
    sg = ShiftingGraph()

    i=0

    first_pass_flag = 1


    min = -1
    max = -1
    mean = 0

    N = 200
    for j in range(N):
        i=i+1

        t = time_ns()
        sg.updateViz(i)
        t_new = time_ns()
        
        diff = t_new - t
        t = t_new
        if(diff < min or min<0):
            min = diff
        if diff > max:
            max = diff
        mean += diff
        
        print(diff/toSec, "s")
        

    print(f"min = {min/toSec} \nmax = {max/toSec}\nmean = {mean/(N*toSec)}")

        

