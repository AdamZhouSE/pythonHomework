def find_pairs(a, n):
    Hash = {}
    sign=[]
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = a[i] + a[j]
            if sum in Hash.keys():
                Hash[sum].append((a[i],a[j]))
                sign.append(sum)
            else:
                Hash[sum]=[(a[i],a[j])]
    if len(sign)==0:
        return False
    min_value=min(sign)
    prev=Hash.get(min_value)
    A,B,C,D=prev[0][0],prev[0][1],prev[1][0],prev[1][1]
    print(a.index(A),a.index(B),a.index(C),a.index(D))
    return True


T=int(input())
for sample in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    if not find_pairs(a,n):
        print("no pairs")