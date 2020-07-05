string = input()
numG = numL = numR = 0
for i in string:
    if i == 'G':
        numG += 1
    elif i == 'R':
        numR += 1
    elif i == 'L':
        numL += 1
if numR - numL % 4 == 0:
    print(False)
else:
    print(True)