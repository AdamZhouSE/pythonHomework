def test9():
    n=int(input())
    x=input().split(" ")
    num = []
    for i in range(n):
        num.append(int(x[i]))
    num.sort()
    if n==2:
        return 0
    a=num[n-2]-num[0]
    b=num[n-1]-num[1]
    if a>b:
        return b
    else:
        return a
print(test9())