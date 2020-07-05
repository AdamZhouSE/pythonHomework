def get(n):
    if n==0:
        return 2
    if n==1:
        return 1
    return get(n-1)+get(n-2)

num=int(input())
for k in range(num):
    n=int(input())
    print(get(n))
    