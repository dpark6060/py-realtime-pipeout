# py-realtime-pipeout


## Realtime output from a python pipe

This file outlines some things I've tried to get well-behaved real time output.  Suggestions are welcome.

As it stands, the best solution I can find is the following:

```
result = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False)

while True:
    line = result.stdout.readline()
    if not line: break
    else:
        print(line)
```

Things to note when using `Popen()` instead of `run()`

- `stdout, stderr = result.communicate()` no longer works, stdout buffer has been emptied with the readline() statement
  - in this example, stdout and stderr are both = ''
- trying to read stderr in the while loop hangs till the command is completed (makes sense as errors cause the program to end)
- Lists of three things are always better than lists of two.
