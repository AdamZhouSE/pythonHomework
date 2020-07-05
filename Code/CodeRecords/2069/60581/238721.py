import sys

lst = []
for line in sys.stdin:
    if line == '':
        break
    lst.append(line)
    
num1 = int(lst[0])
num2 = int(lst[1])

answer = num1 * num2
print(answer)