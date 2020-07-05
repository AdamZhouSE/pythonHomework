import sys


Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

a = int(Input[0])
li = Input[1].split(",")
temp = ""
for item in li:
    temp += item
b = int(temp)

print(a**b%1337)
