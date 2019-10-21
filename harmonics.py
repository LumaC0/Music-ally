def give_directions():
    print('This harmonic caluclator will give harmonic frequencies based on the inputed root frequency')
    print('Input the root frequency (Hz)')

def calculate(root):
    harm = root
    dicts = {}
    for i in range(2,8):
        root += harm
        dicts[i] = root
    return dicts

def main():
    give_directions()
    root = float(input('Frequency(Hz): '))
    print()
    dicts = calculate(root)
    print(f'''1st Harmonic: {root:15}Hz
2nd Harmonic: {dicts[2]:15.3f}Hz
3rd Harmonic: {dicts[3]:15.3f}Hz
4th Harmonic: {dicts[4]:15.3f}Hz
5th Harmonic: {dicts[5]:15.3f}Hz
6th Harmonic: {dicts[6]:15.3f}Hz
7th Harmonic: {dicts[7]:15.3f}Hz
     ''')

main()

