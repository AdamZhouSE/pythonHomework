def findComponents(A):
    p = list(range(len(A)))

    def find(x):
        if x != p[x]:
            p[x] = find(p[x])
        return p[x]


    for i in range(len(A)):
        for j in range(len(A)):
            if hasCD(A[i], A[j]):
                px, py = find(i), find(j)
                if px != py:
                    p[px] = py
                    
    for _ in range(len(p)):
        for k in range(len(p)):
            p[k] = p[p[k]]
    return p.count(max(p, key=p.count))

def hasCD(num1,num2):
    smaller = num1 if num1 < num2 else num2
    for i in range(2, smaller+1):
        if num1 % i == 0 and num2 % i == 0:
            return 1
    return 0

A = list(map(int,input().split(',')))
print(findComponents(A))