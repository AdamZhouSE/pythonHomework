n=int(input())
result=[]

for i in range(n):
    num=int(input())
    if num==1: result.append(6)
    if num==2: result.append(5)
    if num == 3: result.append(4)
    if num==4: result.append(3)
    if num==5: result.append(2)
    if num==6: result.append(1)
for i in range(len(result)):
    print(result[i])