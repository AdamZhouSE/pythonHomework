import sys

lst = []
for line in sys.stdin:
    if line.strip()=='':
        break
    lst.append(line)

number = int(lst[0])

count = 0
begin = 1
while count < number:
    total = []
    for num in range(0,3):
        length = []
        i = 0
        while i < len(lst[begin + num]):
            str = ''
            if lst[begin + num][i] >= '0' and lst[begin + num][i] <= '9':
                str += lst[begin + num][i]
                if i == len(lst[begin + num]) - 1:
                    length.append(int(str))
                    break
                while lst[begin + num][i + 1] >= '0' and lst[begin + num][i + 1] <= '9':
                    str += lst[begin + num][i + 1]
                    i += 1
                    if i == len(lst[begin + num]) - 1:
                        break
                length.append(int(str))
            i += 1
        total.append(length)

    hello = total[1]
    for i in range(0,len(total[2])):
        hello.append(total[2][i])
    hello.sort()
    print(hello[total[0][2]-1])

    begin += 3
    count += 1