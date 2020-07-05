n=int(input())
a=list(map(int,input().split()))
suma=0
sumb=0
for num in a:
    if num<0:
        sumb+=num
    else:
        suma+=num
print(suma-sumb)