n,h = map(int,input().split())
a=[int(n) for n in input().split()]
num=n
for i in range(0,len(a)):
    if h<a[i]:
        num =num+1
print(num)