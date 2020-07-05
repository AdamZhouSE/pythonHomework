n = int(input())
m = int(input())
usds = []
current = 0
for i in range(n):
    usds.append(int(input()))
usds.sort(reverse=True)
for i in range(n):
    current+=usds[i]
    if current>=m:
        print(i+1)
        quit()