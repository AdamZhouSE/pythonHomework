str1 = input().split()
n = int(str1[0])
m = int(str1[1])
ci = input().split()
A = []
for i in range(m):
    string = input().split()
    x = int(string[0]) - 1
    y = int(string[1]) - 1
    if int(ci[x]) > int(ci[y]):
        A.append(x)
    else:
        A.append(y)
count = 0
for i in range(n):
    if i not in A:
        count += int(ci[i])
print(count)
