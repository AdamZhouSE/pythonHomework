n=int(input())
num=list(map(int,input().split()))
top=max(num)
out=0
for i in num:
    out+=top-i
print(out)