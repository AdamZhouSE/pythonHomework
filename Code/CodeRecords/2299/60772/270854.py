
def insert(x,a,i):
    if x < a[i]:
        if a[2*i] == -1:
            a[2*i] = x
        else:
            insert(x,a,2*i)
    else:
        if a[2*i+1] == -1:
            a[2*i+1] = x
        else:
            insert(x,a,2*i+1)

node = []
now = []
for i in range(500):
    node.append(-1)
n = int(input())
line = input()
Len = len(line)
for i in range(Len):
    temp = int(line[i])
    insert(temp,node,0)
while True:
    new_line = input()
    if new_line[0]=='0':
        break
    for i in range(500):
        now.append(-1)
    len1 = len(new_line)
    for i in range(len1):
        temp = int(new_line[i])
        insert(temp,now,0)
    if len1 != Len:
        print("NO")
        continue
    same = True
    for i in range(500):
        if now[i] != node[i]:
            same = False
            break
    if same:
        print("YES")
    else:
        print("NO")

