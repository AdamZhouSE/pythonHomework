nums=list(map(int,input().split(',')))
k=int(input())
ma=max(nums)-k
mi=min(nums)+k
if mi>=ma:
    print(0)
else:
    print(ma-mi)