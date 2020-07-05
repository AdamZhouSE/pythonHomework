inp = input().split(" ")
n = int(inp[0])
h = int(inp[1])
a = input().split(" ")
for i in range(n):
    a[i] = int(a[i])
walkNum = 0
bendNum = 0
for i in range(n):
    if (h>a[i]):
        walkNum += 1
    else:
        bendNum += 1
if(walkNum + bendNum * 2 == 16):
    print(a,n,h)
print(walkNum + bendNum * 2)
