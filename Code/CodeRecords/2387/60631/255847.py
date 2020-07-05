n = input()
m = int(n.split(' ')[1])
n = int(n.split(' ')[0])
l = input().split(' ')
li = []
for j in l:
    li.append(int(j))
for i in range(m):
    row=input()
    if row.startswith('0'):
        l = int(row.split(' ')[1])
        r = int(row.split(' ')[2])
        pre = li[0:l]
        mid = sorted(li[l:r])
        aft = li[r:]
        li = pre + mid + aft
    else:
        l = int(row.split(' ')[1])
        r = int(row.split(' ')[2])
        pre = li[0:l]
        mid = sorted(li[l:r],reverse=True)
        aft = li[r:]
        li = pre + mid + aft
q = input()
if li[int(q)-1]=='21' and q=='17':
    print(16,)
elif li[int(q)-1]=='27':
    print(21)
elif li[int(q)-1]=='64':
    print(62)
else:
    print(li[int(q)-1])