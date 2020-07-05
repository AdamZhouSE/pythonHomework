firstLine = input()
LEN = int(firstLine.split()[0])
NUM = int(firstLine.split()[1])
lst = [int(input()) for i in range(NUM)]
result=[]
for i in range(NUM):
    result.append(lst[i]%LEN)

result999=[]
for i in range(NUM-1):
    for j in range(i+1,NUM):
        if result[i]==result[j] and j not in result999:
            result999.append(j)
result999.sort()
if len(result999)==0:
    print(-1)
else:
    print(result999[0]+1)
