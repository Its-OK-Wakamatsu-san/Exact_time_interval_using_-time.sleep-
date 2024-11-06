# Precise time intervals using "time.sleep"

### Keyword
Python , module , method , precise , interval time , time.sleep , threading , queue , update 

## Overview
We often use "time.sleep" in our measurements, but "time.sleep" gives us the approximate time requested, but not the exact time.
We can set the time interval precisely by adjusting the sleep period using "time.sleep".
### Case#1
Case#1 is when using "time.sleep" , "threading", and "queue".[^1]  　I'll adjust the "time.sleep" period at the end of a series of threading processes.

### Case#2
Case#2 is when not using "threading". For example, when using "matplotlib FuncAnimation" method, I shall adjust "time.sleep" period in the " update function".
   
### Hardware Environment
  1. PC: windows PC
     
### Software Environment
  1. OS: Windows11
  2. Python: Version 3.9.13
  3. Libraries: numpy, matplotlib
     
### Known issue
  1. None
     
### Rerated Webpages
[^1]: [How to run and verify periodically in Python,  described in Japanese](https://qiita.com/montblanc18/items/05715730d99d450fd0d3))
