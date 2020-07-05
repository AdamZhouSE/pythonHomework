n=int(input())
num=[int(i) for i in input().split()]
if not sum(num)%3==0:
    print(0)
else:
    re=0
    for i in range(1,n-1):
        for j in range(i+1,n):
            if sum(num[0:i])==sum(num[i:j]) and sum(num[0:i])==sum(num[j:]):
                re+=1
    print(re)