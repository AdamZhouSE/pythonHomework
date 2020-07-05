[k,n]=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
start=1
for i in arr:
    if n%i==0:
        if i>start:
            start=i
print(n//start)