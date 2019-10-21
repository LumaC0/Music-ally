import termcolor
# instructions and promt user for note -----> need to figure out input frequency. frequency range within notation 
def instructions_query():
    print('''This program will return frequency, scale, and harmonic information for the value specified''')
    print()
    notation = input('Input a note or frequency to see the information associated: ')
    notation = notation.upper()
    return notation

def interpret(notation, step_note_freq):
    if notation in [item for sublist in step_note_freq for item in sublist]:
        for sublist in step_note_freq:
            if sublist[0] == notation:
                step = int(sublist[1])
            else: continue
        return step
    else: print('not a musical note')
    
''' try:
pass step
except expression as identifier:
pass'''



def main():
    step_note_freq = [
    ['A', 1], 
    ['A#', 2], 
    ['B', 3], 
    ['C', 4], 
    ['C#', 5], 
    ['D', 6], 
    ['D#', 7], 
    ['E', 8], 
    ['F', 9], 
    ['F#', 10], 
    ['G', 11], 
    ['G#', 12]]
    #print(type(step_note_freq[1][1]))      shows data type of list element
    #changes data type of list[i][1] to string so input of either note or step can be read and iterprited
    for sublist in step_note_freq:
        sublist[1] = str(sublist[1])
    #query user
    notation = instructions_query()

    #return index of given note
    step = interpret(notation, step_note_freq)
    print(step)
    
    # Reads if value is in the list .... determines whether someone has entered a note or a frequency
    # right now only notes are in list
    
main()
'''#def freq():
#print(440*((2**(1/12))**4))


# notes of minor scale
def minor_note(note, steplist):
    for i in range(len(steplist)):
        if i == 1 or i == 4 or i == 6 or i == 9 or i == 11:
            continue
        else: print(steplist[i][0])


   

def main():
    note = input("Input a note to find its frequency, minor scale, octive series and harmonic series: ")
    note = note.upper()
    step_note_freq = [['A', 1], ['A#', 2], ['B', 3], ['C', 4], ['C#', 5], ['D', 6], ['D#', 7], ['E', 8], ['F', 9], ['F#', 10], ['G', 11], ['G#', 12], ['A', 13]]
    minor_note(note, step_note_freq)



main()



p = pow(2, 1/1/12)

freq = 440 * (p**5)

print(round(freq,2))'''