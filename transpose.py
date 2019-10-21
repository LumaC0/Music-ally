'''old_BMP = int(input("What BPM are you working at?" ))
transposition_steps = int(input("How many steps would you like to transpose?"))

print(old_BMP * (1.05946 ** transposition_steps))'''

print("Input current BPM and steps you'd like to transpose")

bpm = int(input("BPM: "))
trans = int(input("Transposition steps: "))

print(f" New BPM: {bpm * (1.05946 ** trans)}")

