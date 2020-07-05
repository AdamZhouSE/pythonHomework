t = int(input())
wordLst = []
for i in range(0,t):
    line = input().split()
    wordLst.append(line[1])
count = 0
for i in range(0,t):
    first = wordLst[i]
    for j in range(0,t):
        second = wordLst[j]
        temp = first + second
        if(temp == temp[::-1]):
            count = count + 1
print(count)