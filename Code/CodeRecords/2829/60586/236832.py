def test9():
    n=int(input())
    x=input().split(" ")
    num = []
    for i in range(n):
        num.append(int(x[i]))
    num.sort()
    min=num[0]
    max=num[n-1]
    a=num.count(min)
    b=num.count(max)
    return n-a-b
print(test9())
