num=int(input())
l=list(map(int,input().split()))
f=0.000000
for i in range(num):
    f+=l[i]
f=f/num
print(format(f,'.6f'))