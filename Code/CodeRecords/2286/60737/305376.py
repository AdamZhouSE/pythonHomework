con = [int(i) for i in input().split( )]
L, M = con[0], con[1]
tree = [1] * (L+1)
while M:
    cmd = [int(i) for i in input().split( )]
    sta, end = cmd[0], cmd[1]
    for i in range(sta, end+1):
        tree[i] = 0
    M -= 1
cnt = 0
for j in tree:
    if j==1:
        cnt += 1
print(cnt)
