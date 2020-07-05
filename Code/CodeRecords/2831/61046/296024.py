num=int(input())
dict=input().split()
dict=list(map(int,dict))
p=input().split()
s=int(p[0])
t=int(p[1])
if t>s:
    t,s=s,t
sum1=0
for i in range(t-1,s-1):
    sum1+=dict[i]
sum2=sum(dict)-sum1
print(min(sum1,sum2))