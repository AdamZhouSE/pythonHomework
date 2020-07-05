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
    lineNumber = int(lst[begin])
    if lineNumber < 3:
        print(0)
        begin += 2
        count += 1
        continue
    length = []
    i = 0
    while i < len(lst[begin+1]):
        str = ''
        if lst[begin+1][i]>='0' and lst[begin+1][i]<='9':
            str += lst[begin+1][i]
            if i==len(lst[begin+1])-1:
                length.append(int(str))
                break
            while lst[begin+1][i+1]>='0' and lst[begin+1][i+1]<='9':
                str += lst[begin+1][i+1]
                i += 1
                if i == len(lst[begin + 1]) - 1:
                    break
            length.append(int(str))
        i += 1

    triangles = 0
    for i in range(0,lineNumber-2):
        for j in range(i+1,lineNumber-1):
            for h in range(j+1,lineNumber):
                judge = True
                if (length[i]+length[j]<=length[h]) or (length[j]+length[h]<=length[i]) or (length[i]+length[h]<=length[j]):
                    judge = False
                if judge:
                    triangles += 1
    print(triangles)


    begin += 2
    count += 1