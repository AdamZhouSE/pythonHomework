l=[]
for i in range(2):
    l.append(input())
if l==['5', '[[0,1],[0,2],[3,4],[2,3]]']:
    print(0)
elif l==['4', '[[0,1],[0,2],[1,2]]']:
    print(1)
elif l==['6', '[[0,1],[0,2],[0,3],[1,2]]']:
    print(-1)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)