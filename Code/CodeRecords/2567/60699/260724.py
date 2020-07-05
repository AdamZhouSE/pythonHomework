str=input()
str=str[1:len(str)-1]
list1=list(map(int,str.split(',')))
lower=int(input())
upper=int(input())
tot=[]
tot.append(list1[0])
for i in list1:
    tot.append(tot[len(tot)-1]+i)
res=0
for i in range(0,len(tot)):
    for j in range(0,i):
        if tot[i]-tot[j]>=lower and tot[i]-tot[j]<=upper:
            res+=1
print(res)
