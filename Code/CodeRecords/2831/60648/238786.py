n=input()
n=int(n)
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
s,t=map(int,input().split(" "))
sum1=0
sum2=0
for x in ls:
    sum1=sum1+x
if s==t:
    print(0)
    pass
elif s>t:
    s,t=t,s
for j in range(s-1,t-1):
    sum2=sum2+ls[j]
if sum2<=(sum1/2):
    print(sum2)
else:
    print(sum1-sum2)