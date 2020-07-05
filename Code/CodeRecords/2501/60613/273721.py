NUM=int(input())
lstBef=input().split()
lstAft=input().split()
num=[]

for i in lstAft:
    index=lstBef.index(i)
    num.append(index)
result=0
for i in range(NUM-1):
    for j in range(i+1,NUM):
        if num[j]-num[i]<0:
            result+=1

print(result)