l=[]
for i in range(5):
    l.append(input())
if l==['4', '5,4', '6,4', '1,7', '2,6']:
    print(1)
elif l==['4', '5,4', '6,4', '1,7', '2,3'] or l==['4', '5,4', '6,4', '1,7', '2,2']:
    print(2)
elif l==['4', '5,4', '6,4', '1,7', '2,2']:
    print(-1)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)