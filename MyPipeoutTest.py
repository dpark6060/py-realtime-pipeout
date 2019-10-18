#!/usr/bin/env python3


import time
import subprocess as sp




cmd=['/Users/davidparker/Documents/Flywheel/SSE/MyWork/Sandbox/MyEcho.sh','a'] 
result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:
    line = result.stdout.readline()
    if not line: break
    else:
    	print(line)
