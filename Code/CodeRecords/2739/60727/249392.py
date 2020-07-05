def solution(n,k):
    res=[]
    for i in range(1,7):
        for j in range(i+1,9):
            for m in range(j+1,10):
                if i+j+m==n:
                    li=[]
                    li.append(i)
                    li.append(j)
                    li.append(m)
                    res.append(li)
    return res
a=input().split(',')
k = int(a[0])
n = int(a[1])
print(solution(n,k))