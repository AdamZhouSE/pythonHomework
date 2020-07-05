from collections import Counter

NUM=list(map(int,input().split()))
QA=NUM[1]
lst=[input().split() for i in range(NUM[0])]
pointer=0
result=[]

for i in lst:
    step = int(i[0])
    if i[1]=="R":
        for i in range(step):
            result.append(pointer)
            pointer+=1
    else:
        for i in range(step):
            pointer -= 1
            result.append(pointer)

result888=Counter(result)

result999=[]
result000=0
for k,v in result888.items():
    result999.append(v)
for i in result999:
    if i>=QA:
        result000+=1

print(result000,end="")


