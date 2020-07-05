n=int(input())
l=list(map(int,input().split()))
power=0
coin=l[0]
for i in range(0,n-1):
    power+=l[i]-l[i+1]
    if power<0:
        coin+=-power
        power=0
print(coin)      