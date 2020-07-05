n = int(input())
a = list(map(int, input().split(" ")))
n1 = a.count(1)
n2 = a.count(2)
if n1 <= n2:
    print(n1)
else:
    print(n2 + (n1-n2)//3)