n=int(input())
lis=list(map(int,input().split(" ")))
a,b=(map(int,input().split(" ")))
re=0
for i in range(min(a,b)-1,max(a,b)-1):
    re=re+lis[i]
all_=0
for i in range(0,n):
    all_+=lis[i]
if(re<all_-re):
    print(re)
else:
    print(all_-re)