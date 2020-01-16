import csv
import pandas as pd
import matplotlib as mt

pitch = pd.read_csv('/Users/spencerfinkel/repos/musically/pitch_freq.csv')
pitch = pitch.rename(columns={'Unnamed: 2': 'Octive'})
p = (list(pitch))
freq = pitch['Frequency (Hz)']

freq.()




'''#frequency of all notes in a scale
for i in range(13):
    freq = 16.35
    freq1 = freq*((2**(1/12))**i)
    print(f'{freq1:.2f}')


#list comprehension, whole octive frequencies
freq = 73.42
freqsincomprehension = [float(freq*((2**(1/12))**i)) for i in range(13)]
for item in freqsincomprehension:   
    print('{:.2f}'.format(item))
print()



#frequencies of minor scale
def minor_freq(*args):
    for i in range(13):
        freq1=freq
        freq1=freq*((2**(1/12))**i)
        if i == 1 or i ==4 or i == 6 or i == 9 or i ==11:
            continue
        else:
            print(f'{freq1:.2f}')


minor_freq(freq)
print()


#all the octaves of the frequency
def octive(arg):
    print()
    series = [arg]
    if arg > 16.35:
        arg1 = arg
        for oct in range(8):
            arg1/=2
            series.insert(0, arg1)
        for oct in range(8):
            arg *= 2
            series.append(arg)
    else: 
        for oct in range(8): 
            arg *= 2
            series.append(arg)
    series1 = [item for item in series if item <= 7902.13 and item >= 1.00]
    #[enumerate(item) for item in series if item >= 16.35]
    print(series1)

def main():
    freq = float(input('What frequency are you looking for: '))
    octive(freq)

main()'''
