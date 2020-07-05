from sys import stdin
for line in stdin:
    n=int(line)
    arr=list(map(int,input().split()))
    d=int(input())
    a=arr[2**(d-1)-1:2**(d)-1]
    if len(a)==0:
        print("EMPTY")
    else:
        print(' '.join(str(i) for i in a))