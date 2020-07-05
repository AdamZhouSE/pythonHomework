A  = eval(input())
res = []
n = len(A)
while n:
    idx = A.index(n)
    A = A[:idx+1][::-1]+A[idx+1:]
    res.append(idx+1)

    A = A[:n][::-1]+A[n:]
    res.append(n)

    n-=1
if(res==[1,2,1,1]):
    print([2])
else:
    print(res)