n=int(input())
l=input().split(" ")
max_,min_=0,0
for i in range(n):
    if int(l[i])>int(l[max_]): max_=i
    if int(l[i])<int(l[min_]): min_=i
res=0

if max(max_,min_)-0>n-1-min(max_,min_):
    res=max(max_,min_)-0
else:
    res=n-1-min(max_,min_)
print(res)