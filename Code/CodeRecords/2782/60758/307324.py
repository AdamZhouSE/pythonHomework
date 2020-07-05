num=[]
for _ in range(int(input())):
    num.append(int(input()))
mm=[0 for i in range(len(num))]
mm[0]=num[0]
for i in range(1,len(num)):
    cm=1000000
    for j in range(0,i):
        x=abs(num[i]-num[j])
        if(x<cm):
            cm=x
    mm[i]=cm
print(sum(mm),end='')