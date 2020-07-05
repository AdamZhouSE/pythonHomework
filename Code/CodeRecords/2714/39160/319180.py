words = []

try:
    while True:
        words.append(input())
except EOFError:
    pass

start = words[0]
for i in words:
    if len(i) < len(start):
        start = i
        ind = words.index(start)

ans = []
ans.append(start)

for i in words:
    li1 = list(start)
    li2 = list(i)
    if (set(li1) < set(li2)) and (len(i) == len(start)+1):
        ans.append(i)
        start = i
        
print(len(ans))
for i in ans:
    print(i)