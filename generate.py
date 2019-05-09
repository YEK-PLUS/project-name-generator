#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import random
import sys
import time
def choiceChar(v):
    vo = "AEIOU"
    co = "BCDFGHJKLMNPQRSTVXZ"
    return (vo if v  else co)[random.randint(0,len(vo)-1 if v  else len(vo)-1)]

print("\t\t\t"+"set type of word");
def choice():
    print("\n")
    print("\t\t\t"+"vowal|v");
    print("\t\t\t"+"consonant|c");
    print("\t\t\t"+"ex:vcvcc");
    print("\n")
    print("\t\t\t"),
    type = raw_input();
    print("\n")

    a = True
    while a == True:

        try:
            time.sleep(0.1)
            print("\n")
            print("\t\t\t"),
            for types in type:
                sys.stdout.write(choiceChar(True if types == "v" else False)),
                pass
        except (KeyboardInterrupt, SystemExit):
            a = False
        pass

while True:
    choice()
    pass


#POWERED BY YEK
