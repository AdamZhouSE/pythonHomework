n = int(input())
list1 = [[] * n] * n
for i in range(n):
    list1[i] = list(input())
bl = True
x = list1[0][0]
y = list1[0][1]
for i in range(n):
    for j in range(n):
        if j == i or j == abs(n - 1 - i):
            if list1[i][j] != x:
                bl = False
                break
        else:
            if list1[i][j] != y:
                bl = False
                break
    if bl == False:
        break
print("YES" if bl and x!=y else "NO")
