t = int(input())
for _ in range(t):
    n=int(input())
    arr=[int(x) for x in input().split(" ")]
    k=int(input())
    result=1
    for i in arr:
        result*=i
    print(result%k)