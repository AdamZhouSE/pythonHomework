num=int(input())
t=input().split()
t=list(map(int,t))
page=[]
for i in range(1,num+1):
    page.append(i)
day=0
can=0
for i in range(num):
    if t[i]<=page[i] :
        for j in range(i):
            if t[j]<=page[i]:
                can=1
        if can==1:
            day+=1
print(day)