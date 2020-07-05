def func30(arr):
    arr.sort()
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            m=int(arr[i])
            n=int(arr[j])
            while n%m!=0:
                tmp=n%m
                n=m
                m=tmp
            if m==1:
                return True
    return False
ip=input().split(",")
op=func30(ip)
print(op)