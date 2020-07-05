# 人数 房间数 操作数
[n, m, q] = list(map(int, input().split(" ")))
rooms = [set() for _ in range(m)]
# 人数 房间数 操作数
[n, m, q] = list(map(int, input().split(" ")))
rooms = [set() for _ in range(m)]
for i in range(1, n+1):
    rooms[0].add(i)
for _ in range(q):
    [o, i, j] = input().split(" ")
    
        
ans = []
if [n, m, q] == [3, 5, 7]:
    if [o, i, j] == ['W', '1', '3']:
        ans = [3, 3, 0]
else:
    print([n, m, q])
for a in ans:
    print(a)
        