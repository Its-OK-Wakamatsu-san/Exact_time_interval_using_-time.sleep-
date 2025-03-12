#This script will print the elapsed time exactly every second.
#'start_time' records the time the script started.
#'previous_time' records the end time of the last iteration.
#'last_printed_second' records the number of seconds the elapsed time was last printed.
#In the while loop, we get the current time and fold it into 'current_time'.
#'elapsed_time' calculates the amount of time elapsed since the 'start_time'.

import time
import csv
from datetime import datetime
import os

class Application:
    def __init__(self, duration=20):
        self.duration = duration
        self.start_time = None
        self.previous_time = None
        self.eps  = 0.015625 #  1/64 seconds

    def adjust_time(self):
        current_time = time.time()
        self.elapsed_time = current_time - self.start_time
        self.iteration_time = current_time - self.previous_time
        self.previous_time = current_time
        self.sleep_time = 1 - (self.elapsed_time % 1)
        # to prevent negative seconds. 1/64 seconds is added.
        if self.sleep_time <= self.eps:
            self.sleep_time = self.eps
        return

    def print_elapsed_time(self):
        self.start_time = time.time()
        self.previous_time = self.start_time
        last_printed_second = -1

        while True:
            self.adjust_time()

            if int(self.elapsed_time) != last_printed_second:
                last_printed_second = int(self.elapsed_time)
                print(f"Elapsed time: {self.elapsed_time:.3f} seconds, Iteration time: {self.iteration_time:.3f} seconds",
                      f", sleep time: {self.sleep_time:.3f} seconds")

            if self.elapsed_time >= self.duration:
                break
            
            time.sleep(self.sleep_time)

    def run(self):
        self.print_elapsed_time()

if __name__ == "__main__":
    app = Application(duration=1000)
    app.run()
