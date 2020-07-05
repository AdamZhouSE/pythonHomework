n=eval(input())
arr=str(bin(n))
arr=list(arr[2:])
s=-1
e=-1
step=0
for i in range(len(arr)):
    if arr[i]=='1':
        if s==-1:
            s=i
        else:
            e=i
            step=max(e-s,step)
            s=e
print(step)