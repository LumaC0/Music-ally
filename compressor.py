#!/usr/bin/env python3

#bpm to millisecond for compressor release

bpm = float(input("BPM: "))
note = input("note length: ")

if note == '1/4':
    desireBe = (60/bpm)*(10**3)
    print(f'{round(desireBe,1)}ms')
elif note == '1/8':
    desireBe = (60/bpm)*(10**3)/2
    print(f'{round(desireBe,1)}ms')
elif note == '1/16':
    desireBe = (60/bpm)*(10**3)/4
    print(f'{round(desireBe,1)}ms')
elif note == '1/32':
    desireBe = (60/bpm)*(10**3)/8
    print(f'{round(desireBe,1)}ms')
elif note == '1/64':
    desireBe = (60/bpm)*(10**3)/16
    print(f'{round(desireBe,1)}ms')
elif note == '1/128':
    desireBe = (60/bpm)*(10**3)/32
    print(f'{round(desireBe,1)}ms')
elif note == '1/256':
    desireBe = (60/bpm)*(10**3)/64
    print(f'{round(desireBe,1)}ms')
else: print("invaled note length")
            
