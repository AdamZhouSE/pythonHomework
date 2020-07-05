a=list(map(int,input().split(',')))
k=int(input())
mid=(max(a)+min(a))/2
b=[]
for i in a:
    if(i>mid):
        b+=[i-k]
    else:
        b+=[i+k]
print(max(b)-min(b))