n = int(input())
a = 2
b = 3
ans = [a, b]
for i in range(0, 98):
    temp = b
    b = a + b
    a = temp
    ans.append(b)
for i in range(0, n):
    temp = int(input())
    print(ans[temp - 1] % (pow(10, 9) + 7))
