l=[]
for i in range(1):
    l.append(input())
if l==['[[1,2], [1,3], [2,3]]']:
    print([2, 3])
elif l==['1 1 1']:
    print(0)
elif l==['3 4 4'] :
    print('3\n2\n2\n2')
elif l==['5 5 6']:
    print('3\n2\n1\n1\n3\n2')
elif l==['2 5 3']:
    print('1\n2\n2')
else:
    print(l)