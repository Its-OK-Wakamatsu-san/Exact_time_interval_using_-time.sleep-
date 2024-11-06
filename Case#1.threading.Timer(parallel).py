# See https://qiita.com/montblanc18/items/05715730d99d450fd0d3
# Pythonで定周期で実行する方法と検証
# [OK] 処理時間を考慮してthreadingとsleepを使う
# threading自分が理解しやすいキューを出して動作させる方法でタイムコントロールしてみた。
# Time_Control -> Proc1 ->return(Time_Control) (parallel)
#              -> Proc2 ->return(Time_Control) (parallel)

# -*- coding: utf-8 -*-
import os.path
import threading
import time
import datetime
import queue
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)

        # Initial Conditions 
        self.stop_threads = False                   # stop threading flag  False = Threading continue.

        master.geometry("400x140")                  # window size(width x height)
        str_prog_name = os.path.basename(__file__)  # get present program name
        master.title( str_prog_name )               # Window Title

         # Label
        lbl_0  = tk.Label(root,text='Time_Control Start')
        lbl_0.place (x=10, y=50)
        lbl_1  = tk.Label(root,text='Process1')
        lbl_1.place (x=10, y=80)
        lbl_2  = tk.Label(root,text='Process2')
        lbl_2.place (x=10, y=110)
        # Text Box
        self.txt_x0 = tk.Entry(root,width=40)
        self.txt_x0.insert(tk.END,'daytime.now().strftime')
        self.txt_x0.place (x=130, y=50)
        self.txt_x1  = tk.Entry(root,width=40)
        self.txt_x1.insert(tk.END,'daytime.now().strftime')
        self.txt_x1.place (x=130, y=80)
        self.txt_x2 = tk.Entry(root,width=40)
        self.txt_x2.insert(tk.END,'daytime.now().strftime')
        self.txt_x2.place (x=130, y=110)

        # Start Button
        self.start_btn = tk.Button(root, text='Start', command=self.Threading_Start) # threading start
        self.start_btn.grid(row=0, column=0, padx=5, pady=5)
        # Stop  Button
        self.start_btn = tk.Button(root, text=' Stop', command=self.Terminate) # threading stop
        self.start_btn.grid(row=0, column=1, padx=5, pady=5)
    
    def Threading_Start(self):
        #Queue(Threading control) 
        queue1 = queue.Queue()
        queue2 = queue.Queue()
        queue3 = queue.Queue()
        queue4 = queue.Queue()
        #Threading 
        t1 = threading.Thread(target=self.Proc1,        args=(queue1,queue2,queue3,queue4))
        t2 = threading.Thread(target=self.Proc2,        args=(queue1,queue2,queue3,queue4))
        t3 = threading.Thread(target=self.Time_Control, args=(queue1,queue2,queue3,queue4))  # threading control
        t1.start()
        t2.start()
        t3.start()
        return
    
    def Time_Control(self,queue1,queue2,queue3,queue4):

        # Initial(local)
        rest_time   = interval_t  = 1.0
        time_old    = time.time()
            
        #Time_Control start  write textBox_0
        str_daytime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        self.txt_x0.delete (0,'end')
        self.txt_x0.insert (tk.END, str_daytime)

        while True:
            # Button break
            if self.stop_threads:
                self.stop_threads = not self.stop_threads
                break

            # threading  queue
            queue1.put('Process1') 
            queue2.put('Process2') 
            # interval time set
            time.sleep(rest_time)
            # threading  queue
            queue3.get('Process1')
            queue4.get('Process2')

            # adjust the rest_time
            time_instant = time.time()
            turnaround_time =  time_instant - time_old
            time_old = time_instant
            rest_time += (interval_t - turnaround_time)
            if rest_time <= 0.001:
                rest_time =0.001
            print(rest_time)
        return
    
    def Proc1(self,queue1,queue2,queue3,queue4):

        while True:
            # threading  queue
            queue1.get()
            
            #Process1   write textBox_1
            str_daytime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            self.txt_x1.delete (0,'end')
            self.txt_x1.insert (tk.END, str_daytime)

            time.sleep(0.9) #   imaginary processing time

            # threading  queue
            queue3.put('from thread Proc_1')
        return

    def Proc2(self,queue1,queue2,queue3,queue4):

        while True:
            # threading  queue
            queue2.get()

            #Process2   write textBox_2
            str_daytime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            self.txt_x2.delete (0,'end')
            self.txt_x2.insert (tk.END, str_daytime)

            time.sleep(1.2) #   imaginary processing time

            # threading  queue
            queue4.put('from thread Proc_2')
        return

    def Terminate(self):
        self.stop_threads = True
        return

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
