n=int(input())
l=list(map(int,input().split()))
Max=1
Sum=1
tmp=l[0]
for i in l[1:]:
    if i>tmp:
        Sum+=1
        Max=max(Max,Sum)
    else:
        Sum=1
    tmp=i
print(Max)