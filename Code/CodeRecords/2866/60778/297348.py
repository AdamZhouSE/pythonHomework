length=int(input())
cho=input().split()
res=1
start=False
count=1
for c in cho:
    if(c=='1'):
        if(start):
            res*=count
            count=1
        else:
            start=True
            count=1
    else:
        count+=1
print(res)