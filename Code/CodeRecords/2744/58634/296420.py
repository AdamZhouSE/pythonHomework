n = int(input())
words = []
for _ in range(n):
    words.append(input().split(" ")[1])
res = 0
for i in words:
    for j in words:
        if list(i+j) == list(reversed(list(i+j))):
            res+=1
print(res)

