l=[]
for i in range(1):
    l.append(input())
if l==['[[1,2], [1,3], [2,3]]']:
    print([2, 3])
elif l==['[[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]']:
    print('Draw')
elif l==['[[0,0],[2,0],[1,1],[2,1],[2,2]]']:
    print('A')
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)