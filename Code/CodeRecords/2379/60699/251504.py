p, d = 0, 1
instructions = input()
for i in instructions:
    d *= (i == 'G') + 1j * ((i == 'L') - (i == 'R'))
    p += d * (i == 'G')
print(p == 0 or d != 1)