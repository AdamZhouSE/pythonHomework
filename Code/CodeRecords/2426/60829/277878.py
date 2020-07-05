n=int(input())
for i in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    b.sort()
    sum=b[a-1]*b[a-2]*b[a-3]
    print(sum)