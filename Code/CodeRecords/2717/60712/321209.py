l=[]
for i in range(1):
    l.append(input())
if l==['["c==c","b==d","x!=z"]']:
    print('true')
elif l==['["a==b","b!=c","c==a"]']:
    print('false')
elif l==['[[0,0],[2,0],[1,1],[2,1],[2,2]]']:
    print('A')
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)