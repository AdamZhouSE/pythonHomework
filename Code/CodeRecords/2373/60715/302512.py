def sum(num):
    count=0
    for i in num:
        count+=i
    return count
T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    an1=[]
    an2=[]
    for i in range(len(num)):
        if i%2==0:
            an1.append(num[i])
        else:
            an2.append(num[i])
    print(max(sum(an1),sum(an2)))
    T-=1