import sys
n,k=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
record=sys.maxsize
for i in arr:
    if(k%i==0):
        if(k/i<record):
            record=(int)(k/i)
print(record)

