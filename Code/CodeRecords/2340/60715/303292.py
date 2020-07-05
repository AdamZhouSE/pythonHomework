T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    summ=[]
    for i in range(len(num)):
        summ.append(min(max(num[0:i+1]),max(num[i:]))-num[i])
    print(sum(summ))
    T-=1