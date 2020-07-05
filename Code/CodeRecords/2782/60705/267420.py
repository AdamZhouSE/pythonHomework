days = int(input())
li = []
for i in range(0, days):
    li.append(int(input()))
f = [li[0]]
for i in range(1, days):
    temp = []
    for j in range(0, i):
        temp.append(abs(li[i] - li[j]))
    f.append(min(temp))
print(sum(f))
