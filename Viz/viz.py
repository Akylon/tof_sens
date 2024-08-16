import matplotlib.pyplot as plt
import numpy as np

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
sg = ShiftingGraph()

while(1):
    input("")
    sg.updateViz(200)
    

