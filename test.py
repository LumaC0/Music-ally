#frequency of all notes in a scale
'''for i in range(13):
    freq = 16.35
    freq1 = freq*((2**(1/12))**i)
    print(f'{freq1:.2f}')'''


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

freq=244
minor_freq(freq)
print()


#all the octaves of the frequency
def octive(arg):
    print()
    series = [freq, ]
    for i in range(8):
        arg *= 2
        series.append(arg)
    print(series)

octive(freq)