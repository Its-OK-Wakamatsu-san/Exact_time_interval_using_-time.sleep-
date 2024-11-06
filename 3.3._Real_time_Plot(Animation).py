# realtime plot using FuncAnimation, animation interval_time adjusted to the correct duration.
import os
import os.path
import time
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)

        self.master.geometry("300x400+0+0")                    # Main Panel window location x=0,y=0
        str_prog_name = os.path.basename(__file__) # get present program name
        self.master.title( str_prog_name )

        # Animation flag running.
        self.isRunning = True

        # Frame4
        frame4 = tk.Frame(root, bd=2, pady=5, padx=5)
        frame4.place(x=20, y=50)
        #label
        label_top = tk.Label(frame4, text='Plot Control Panel')
        label_top.grid(row=0, column=0, padx=5, pady=5)
        label_volt = tk.Label(frame4, text='Amplitude(V)')
        label_volt.grid(row=1, column=0, padx=5, pady=5)
        label_bias = tk.Label(frame4, text='Bias(V)')
        label_bias.grid(row=2, column=0, padx=5, pady=5)
        label_t_interval = tk.Label(frame4, text='dt_time interval (s)')
        label_t_interval.grid(row=3, column=0, padx=5, pady=5)
        label_elapsed_time = tk.Label(frame4, text='Elapsed time(s)')
        label_elapsed_time.grid(row=5, column=0, padx=5, pady=5)
        #text box
        self.en_volt = tk.Entry(frame4, width=10, justify='center')
        self.en_volt.grid(row=1, column=1, padx=5, pady=5)
        self.en_volt.insert(tk.END, str(5))
        self.en_bias = tk.Entry(frame4, width=10, justify='center')
        self.en_bias.grid(row=2, column=1, padx=5, pady=5)
        self.en_bias.insert(tk.END, str(4))
        self.srt_t_interval = tk.Entry(frame4, width=10, justify='center')
        self.srt_t_interval.grid(row=3, column=1, padx=5, pady=5)
        self.srt_t_interval.insert(tk.END, str(0.2))
        self.elapsed_time = tk.Entry(frame4, width=15, justify='center')
        self.elapsed_time.grid(row=5, column=1, padx=5, pady=5) 
        # Exec Button
        button_Plot = tk.Button(frame4, text='Brand New Plot', command=self.Plot_Framework, width=15, height=2)
        button_Plot.grid(row=4, column=0, padx=5, pady=5)
        button_Plot = tk.Button(frame4, text='Pause/Resume Plot', command=self.__Pause_Resume, width=15, height=2)
        button_Plot.grid(row=4, column=1, padx=5, pady=5)    


    # Real_Time_Plot but asynchronus
    def Plot_Framework(self):
        # start time
        self.time_start = self.time_old = time.time()
        # Read & Set  time inteval
        self.amplitude = float(self.en_volt.get())
        self.bias = float(self.en_bias.get())
        self.dt   = float(self.srt_t_interval.get())
        t_plot    = 10          # msec  Plot time (animation interval) is experimentally set and is shorter than the actual time.
        self.rest_time = self.dt - t_plot/1000. 
        #  plot data
        self.x = [0]
        self.y0 = [0]
        self.y1 = [self.bias + self.amplitude * np.sin(self.dt * self.x[-1])]
        self.y2 = [self.bias + self.amplitude * np.cos(self.dt * self.x[0])]

        # step2 graph frame
        self.fig, self.ax = plt.subplots(figsize=(12, 6))
        
        #  graph Legend
        self.ax.set_xlabel('Measured Point [$N.D.$]')
        self.ax.set_ylabel('Amplitude [$V$]')
        Label_1 = 'Sine(t)'
        Label_2 = 'Cosine(t)'

        self.ln1, = plt.plot(self.x, self.y1, color='C0', linestyle='-', label=Label_1)
        self.ln2, = plt.plot(self.x, self.y2, color='C1', linestyle='--', label=Label_2)
        self.ax.legend()

        self.anim = FuncAnimation(self.fig, self.__update, interval=t_plot)    
        plt.get_current_fig_manager().window.wm_geometry("+300+0")  # Plot window location x=300,y=0
        plt.show()
        return

    def __update(self,frame):
        # time control
        time.sleep(self.rest_time)
        #elapsed_time
        time_instant = time.time()
        elapsed_t = time_instant - self.time_start
        self.elapsed_time.delete(0,'end')
        self.elapsed_time.insert(0, f'{elapsed_t:.3f}') #  ←小数点以下3桁表示

        #  plot data update
        self.x.append(self.x[-1] + 1)
        self.y0.append(elapsed_t)
        self.y1.append(self.bias + self.amplitude * np.sin(self.dt * self.x[-1]))
        self.y2.append(self.bias + self.amplitude * np.cos(self.dt * self.x[-1]))
    
        self.ln1.set_data(self.x, self.y1) 
        self.ln2.set_data(self.x, self.y2) 
        self.fig.gca().relim()          #grapgh cal re-calculate limit
        self.fig.gca().autoscale_view() #grapgh cal autoscale

        # rest_time(self.rest_time) is adjested to the required time_interval(self.dt)
        turnaround_time =  time_instant - self.time_old
        self.time_old = time_instant
        self.rest_time += (self.dt - turnaround_time)
        if self.rest_time <= 0.001:
            self.rest_time =0.001
        print('turnaround_time = ',  f'{turnaround_time:.3f}',',  sleep_set_time = ',  f'{self.rest_time:.3f}')
        return
    
    # "Pause/Resume" is executed, when button is clicked. Running status is toggled.
    def __Pause_Resume(self):
        if self.isRunning:
            self.anim.event_source.stop()
            self.isRunning = not self.isRunning
        else:
            self.anim.event_source.start()
            self.isRunning = not self.isRunning
        return

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()