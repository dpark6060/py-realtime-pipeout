#!/usr/bin/env python3

import time
import subprocess as sp
import sys

"""
Real time output from a command line process is extremely finicky.
This first example is probably the best, though it is a continuous while loop.
The following examples explain why other things don't work.
"""


cmd=['/Users/davidparker/Documents/Flywheel/SSE/MyWork/Sandbox/MyEcho.sh','15'] 
result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:
    line = result.stdout.readline()
    if not line: break
    else:
        print(line)


"""
Adding a line to read the standard error results in the while loop hanging
until the process has completed.  This is (probably) because the stderror waits
until the end of excecution to collect errors and return a value.  
"""


result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:
    line = result.stdout.readline()
    err = result.stderr.readline()
    if not line: break
    else:
        print(line)
    if err:
        print(err)
        break



"""
We can verify that this is due to the presence of the results.stderr by commenting
it out and leaving the pring err statement.
"""

err=''
result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:
    line = result.stdout.readline()
    #err = result.stderr.readline()
    if not line: break
    else:
        print(line)
    if err:
        print(err)
        break


"""
You may want to wait a few seconds and then read in multiple lines at once to avoid
crunching through a while loop for the entire execution.  Unfortunately, calling "readlines()"
causes the program to wait for the completion of the command, which defetes the purpose of this.
"""


result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:
    time.sleep(1)
    line = result.stdout.readlines()
    if not line: break
    else:
        for l in line:
            print(l)

"""
Introducing a sleep, and continuing to use "readline()" results in a delayed (slower) readout 
of each line of the pipe.  Again, useless.
"""


result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:
    time.sleep(6)
    line = result.stdout.readline()
    if not line: break
    else:
        print(line)



"""
You can wait for the buffer to reach a certain size (say, 100 characters), and only 
print when this happens, however this may result in splitting a single line of the output
into two lines at an arbitrary point.  e.g.:
The output should read:
<90 characters of output>
"This is one output line"

However if the 100th character is in the middle of this line, it could read like this:
<90 characters of output>
"This is on"
"e output line"
"""

result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:    
    line = result.stdout.read(100)
    if not line: break
    else:
        print(line)



