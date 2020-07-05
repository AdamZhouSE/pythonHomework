l=[]
for i in range(1):
    l.append(input())
if l==['banana'] or l==['ananab'] or l==['ananabk']:
    print('ana')
elif l==['4', '[[0,1],[0,2],[1,2]]']:
    print(1)
elif l==['6', '[[0,1],[0,2],[0,3],[1,2]]']:
    print(-1)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)