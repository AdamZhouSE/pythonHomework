ns=input().split(' ')
n=int(ns[0])
s=int(ns[1])
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(n):
    mx_len=0
    k=1
    while 2*k+i<=n:
        sub_sq=a[i:i+2*k]
        if sum(sub_sq[:k])<=s and sum(sub_sq[k:])<=s:
            mx_len=2*k
        k+=1
    print(mx_len)