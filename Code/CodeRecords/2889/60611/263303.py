num=int(input())
l=list(map(int,input().split()))
f=0.0
for i in range(num):
    f+=l[i]
f=f/num
print(round(f,6))