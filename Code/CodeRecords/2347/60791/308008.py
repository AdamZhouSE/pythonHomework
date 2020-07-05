import sys

temp = input().split(' ')
n,m = int(temp[0]),int(temp[1])
line = sys.stdin.readline().strip()
stack = []
mapp = [[-1 for i in range(n)] for i in range(n)]
pare = [-1]*n
used = [-1]*n
while(line):
    this = [int(i)-1 for i in line.split(' ')]
    mapp[this[0]][this[1]] = 1
    line = sys.stdin.readline().strip()


for i in range(m):
    stack.append(i)

while(len(stack)!=0):
    node = stack.pop()
    can_find = False
    is_used = False
    for i in range(m,n):
        if mapp[node][i] == 1 and used[i] == -1:
            used[i] = 1
            used[node] = 1
            pare[i] = node
            break
            mapp[node][i] = 0
            can_find = True
        elif mapp[node][i] == 1:
            is_used = True
    if is_used and not can_find:
        for i in range(m,n):
            if mapp[node][i] == 1:
                mapp[node][i] = 0
                temp = pare[i]
                stack.append(temp)
                pare[i] = node
                used[temp] = 0
res = 0

for i in range(m,n):
	if pare[i] != -1:
		res+= 1
print(res)