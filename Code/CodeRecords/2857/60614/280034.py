length=int(input())
nums=[int(x) for x in input().split()]
count=0
def check(a,b):
    if a<b:
        temp=a
        a=b
        b=temp
    c=a%b
    while c!=0:
        a=b
        b=c
        c=a%b
    return b
GCD=nums[length-1]
for i in range(length-1):
    GCD=check(GCD,nums[i])
i=2
sum=1
while i<=pow(GCD,0.5):
    count=0
    while GCD%i==0:
        GCD/=i
        count+=1
    sum*=count+1
    i+=1
    while i%2==0:
        i+=1
if GCD!=1:
    print(sum*2)
else:
    print(1)