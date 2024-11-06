# Precise time intervals using "time.sleep"

### Keyword
Python , module , method , precise , interval time , time.sleep , threading , queue , update 

## Overview
I often use "time.sleep", but the sleep time is about my required time, but not precise time.
It helps to precise time intervals using "time.sleep" on Python.

### Case#1
Case#1 is when using "time.sleep" , "threading", and "queue". [^1]

### Case#2
Case#2 is when not using "threading". For example, when using "matplotlib FuncAnimation" method, in the update function, I shall adjust "time.sleep" duration.
   
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
