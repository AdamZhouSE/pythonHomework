n = int(input())
m = int(input())
usbS = []
for i in range(0, n):
    usbS.append(int(input()))
usbS.sort(reverse=True)

count = 0
got = 0
for i in range(0, n):
    if got >= m:
        break
    got += usbS[i]
    count += 1
print(count)