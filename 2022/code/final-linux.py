#!/usr/bin/env python3
import subprocess

stid=['c1101561{:02d}'.format(i) for i in range(1,56)]
print(stid)

for i in stid:
    proc=subprocess.Popen(['adduser','--gid','1001',"{}".format(i)],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
out,err=proc.communicate(b"123\n123\n\n\n\n\n\nY\n")
proc.wait()
print(i)
print(out.decode('utf-8'))