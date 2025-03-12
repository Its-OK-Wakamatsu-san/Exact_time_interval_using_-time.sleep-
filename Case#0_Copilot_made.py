#This script will print the elapsed time exactly every second.
#'start_time' records the time the script started.
#'previous_time' records the end time of the last iteration.
#'last_printed_second' records the number of seconds the elapsed time was last printed.
#In the while loop, we get the current time and fold it into 'current_time'.
#'elapsed_time' calculates the amount of time elapsed since the 'start_time'.

import time

def adjust_time( start_time, previous_time):
        current_time = time.time()
        elapsed_time = current_time - start_time
        iteration_time = current_time - previous_time
        previous_time = current_time
        sleep_time = 1 - (elapsed_time % 1)
        return elapsed_time, iteration_time, sleep_time, previous_time

def print_elapsed_time(duration=20):
    start_time = time.time()
    previous_time = start_time
    last_printed_second = -1

    while True:
        # Calculate elapsed time to adjust the time
        elapsed_time, iteration_time, sleep_time,previous_time = adjust_time( start_time, previous_time)

        if int(elapsed_time) != last_printed_second:
            last_printed_second = int(elapsed_time)
            print(f"Elapsed time: {elapsed_time:.3f} seconds, Iteration time: {iteration_time:.3f} seconds",
                  f", sleep time: {sleep_time:.3f} seconds")

        if elapsed_time >= duration:
            break
            
        # Wait until the next second (1 second cycle)
        time.sleep(sleep_time)

def main():
    print_elapsed_time()

if __name__ == "__main__":
    main()
