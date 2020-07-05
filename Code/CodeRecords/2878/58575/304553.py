str=list(map(int,input().split(" ")))
n=str[0]
k=str[1]
bucket=list(map(int,input().split(" ")))
min=999
for i in bucket:
    t=k%i
    if t==0:
        if k%i<min:
            min=k//i

print(min)