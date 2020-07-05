import sys

lst = []
for line in sys.stdin:
    if line.strip() == '':
        break
    lst.append(line)

number = int(lst[0])

str = ''
for i in range(0,len(lst[1])):
    if lst[1][i]>='0' and lst[1][i]<='9':
        str += lst[1][i]

math = pow(number,int(str))%1337

print(math)
