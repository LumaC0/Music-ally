#!/usr/bin/env python3

#bpm to millisecond for compressor release


def compressor_release(bpm, note_length):
    '''
    Inputs: BPM, note length
    Output: compression release time

    Note: Function returns perfect compression release time for standard note lengths. Electronic music is not standard mus    ic so this does not have much of an application
    '''
    # using a tuple because
    standard_lengths = ('1/4', '1/8', '1/16', '1/32', '1/64', '1/128', '1/256')
    
    return round((float(60)/bpm)*(10**3)/2**int(standard_lengths.index(note_length)))

beep = int(input('BPM: '))
length = input('Note length: ')

j = compressor_release(int(beep),length)
print(j)

# ~THIS IS OLD CODE~ 
"""
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
"""            
