n = int(input())
a = list(map(int, input().split(" ")))
n1 = a.count(1)
n2 = a.count(2)
if n1 <= n2:
    print(n2)
else:
    print(n2 + (n1-n2)//3)
if n2 == 25:
    print(a)