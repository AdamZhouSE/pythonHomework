
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
        if i==0:
            can=1
        else:
            can=1
            for j in range(i):
                if t[j]>page[i]:
                    can=0
        if can==1:
            day+=1
print(day)