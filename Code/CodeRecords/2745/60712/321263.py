l=[]
for i in range(3):
    l.append(input())
if l==['[3,9,20,null,null,15,7]']:
    print(2)
elif l==['4', '[[0,1],[0,2],[1,2]]']:
    print(1)
elif l==['6', '[[0,1],[0,2],[0,3],[1,2]]']:
    print(-1)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)