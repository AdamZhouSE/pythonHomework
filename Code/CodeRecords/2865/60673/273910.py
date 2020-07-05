n = int(input())
fileMax = int(input())
content = []
res = 0
for i in range(n):
    content.append(int(input()))
content.sort()
for i in range(n):
    if(fileMax>0):
        fileMax -= content[n-i-1]
        res += 1
    else:
        break
print(res)