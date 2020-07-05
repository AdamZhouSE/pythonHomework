n=int(input())
l=list(map(int,input().split()))
Sum=0
tmp=0
energy=0
for i in l:
    if i>=tmp+energy:
        Sum+=i-tmp-energy
        energy=0
    else:
        energy+=tmp-i
    tmp=i
print(Sum)