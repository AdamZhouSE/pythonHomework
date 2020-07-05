str=input().split()
n=[-1]*int(str[0])
m=int(str[1])
instr=[]
for i in range(m):
    instr.append(int(input()))
for i in instr:
    n[i-1]*=-1
    length=0
    for j in range(0,len(n)):
        k=j
        temp=0
        while k+1<len(n):
            if n[k]+n[k+1]==0:
                temp+=1
                k=k+1
            else:
                temp+=1
                break
            if k==len(n)-1:
                temp+=1
        if temp>length:
            length=temp
    print(length)
