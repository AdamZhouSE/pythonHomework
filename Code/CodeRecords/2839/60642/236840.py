a = int(input())
b = []

for i in range(a):
    c = input()
    b.append(c)
    if (b.count(c)==1):
        print("NO")
    else:
        print("YES")