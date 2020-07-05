nums=list(input())
nn=len(nums)
new=[]
t=1
for k in range(0,5*nn):
    i=t
    if i in range(0,nn):
        if not nums[i].isdecimal():
            t=i+1
            pass
        elif nums[i].isdecimal():
            k=int(nums[i])
            for j in range(i+1,nn-1):
                if nums[j].isdecimal():
                    k=k*10+int(nums[j])
                    t=j+1
                else:
                    t=i+3
                    break
            new.append(k)
    else:
        break
def longest(A):
    n=len(A)
    best=0
    for k in range(0,n):
        i=A[k]
        for j in range(i+1,i+n):
            if j in A:
                t=j-i+1
                if t>best:
                    best=t
            else:
                break
    return best
print(longest(new))
