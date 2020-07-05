bnum=int(input())
boy=[int(n) for n in input().split(' ')]
gnum=int(input())
girl=[int(n) for n in input().split(' ')]
for i in range(0,bnum):
    for j in range(i+1,bnum):
        if boy[i]<boy[j]:
            boy[i],boy[j]=boy[j],boy[i]
for i in range(0,gnum):
    for j in range(i+1,gnum):
        if girl[i]<girl[j]:
            girl[i],girl[j]=girl[j],girl[i]
sum=0
for i in range(0,bnum):
    b = boy[i]
    for j in range(0,gnum):
        if girl[j]==-1:
            continue
        else:
            g=girl[j]
            value=g-b
            if value==-1 or value==1:
                sum=sum+1
                girl[j]=-1
                break
print(sum)