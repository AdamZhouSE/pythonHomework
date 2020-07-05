piles=input()[1:-1].split(',')
piles=list(map(int,piles))
h=int(input())
low=1
high=max(piles)

def able(k):
    t=0
    for pile in piles:
        t+=(pile-1)//k+1 #即p/k向上取整
    return t<=h


for i in range(low,high+1):
    if able(i):
        print(i)
        break