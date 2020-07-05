n=int(input())
l=list(map(int,input().split()))[1:]
Sum=0
tmp=0
energy=0
for i in l:
    if i>=tmp+energy:
        Sum+=i-tmp
    else:
        energy+=i-tmp
    tmp=i
print(Sum)