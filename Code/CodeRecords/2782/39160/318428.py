n = int(input())
li = []

for i in range(n):
    li.append(int(input()))
    
def cal(index):
    m = []
    for i in range(index):
        m.append(abs(li[index] - li[i]))
    return min(m)

ans = li[0]
for i in range(1, n):
    ans+=cal(i)
    
print(ans, end='')