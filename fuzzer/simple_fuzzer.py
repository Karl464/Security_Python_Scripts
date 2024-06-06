#!/usr/bin/python3
"""	
fuzzer script to attack buff.c:

change privileges of script:
	chmod +x simple_fuzzer.py
execute script code: 
	./simple_fuzzer.py buff

Note: Be aware of buzz.c compilation and execution requirements, 
as some protection needs to be disabled on compilation and on OS
in order to enable bufferoverflow.
"""
import subprocess as sp
import time

def fuzz():
    i = 100
    while 1:
        fuzz_str = 'a'*i
        p = sp.Popen("echo "+fuzz_str+" | ./buff", stdin=sp.PIPE,
                        stdout=sp.PIPE, stderr=sp.PIPE, shell=True)

        out = str(p.communicate()[0])
        output = out.split("\\n")

        if "What" in output[0]:
            print(output[0]+"\n" + "\n")
            print("Continue Fuzzing: Length: "+str(i))
            i = i+100
        else:
            print(output)
            print("Application crashed at input length: " + str(i))
            break
    time.sleep(2)

fuzz()
