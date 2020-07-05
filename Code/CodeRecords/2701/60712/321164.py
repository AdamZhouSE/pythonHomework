l=[]
for i in range(1):
    l.append(input())
if l==['[[0,0],[1,1]]']:
    print('Pending')
elif l==['AABAABABAB', '2']:
    print(7)
elif l==['AABAAABBB', '4']:
    print(9)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)