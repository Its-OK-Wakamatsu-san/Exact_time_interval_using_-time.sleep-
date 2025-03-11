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

start_time = time.time()
previous_time = start_time
last_printed_second = -1

# 現在の日付と時間を取得してファイル名に追加
current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'elapsed_time_{current_datetime}.csv'

# プログラムのあるフォルダの直下にファイルを保存
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, filename)

# 現在のスクリプトの名前を取得
script_name = os.path.basename(__file__)

# CSVファイルを開き、コメント行とヘッダーを書き込む
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # コメント行を追加
    writer.writerow([f'# Program: {script_name}, DateTime: {current_datetime}'])
    writer.writerow(['Elapsed Time', 'Iteration Time'])

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        iteration_time = current_time - previous_time
        previous_time = current_time

        if int(elapsed_time) != last_printed_second:
            last_printed_second = int(elapsed_time)
            print(f"Elapsed time: {elapsed_time:.3f} seconds, Iteration time: {iteration_time:.3f} seconds")
            
            # CSVファイルに書き込む
            writer.writerow([elapsed_time, iteration_time])

        # 20秒経過したらループを終了する
        if elapsed_time >= 20:
            break

        # Calculate the time to sleep to correct for any drift
        sleep_time = 1 - (elapsed_time % 1)
        time.sleep(sleep_time)
