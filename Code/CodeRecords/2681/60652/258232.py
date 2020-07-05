def min_operation(n):
    if n==0:
        return 0
    if n%2!=0:
        return min_operation(n-1)+1
    return min(min_operation(n//2),min_operation(n-1))+1


T=int(input())
for i in range(0,T):
    n=int(input())
    print(min_operation(n))