num=int(input())
l=input().split()
sum=0
max=-1
ans=0
for i in range(num):
    if l[i]=="0":
        ans+=1
        if ans>max:
            max=ans
    else:
        ans-=1
        if ans<0:
            ans=0
    if ans<max or ans==0:
        sum+=int(l[i])
print(sum+max)