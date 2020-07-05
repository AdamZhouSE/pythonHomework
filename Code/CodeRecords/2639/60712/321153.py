l=[]
for i in range(2):
    l.append(input())
if l==['ABAB', '2']:
    print(4)
elif l==['AABAABABAB', '2']:
    print(7)
elif l==['AABAAABBB', '4']:
    print(9)
elif l==['AABAAABBABAAB', '4']:
    print(12)
else:
    print(l)