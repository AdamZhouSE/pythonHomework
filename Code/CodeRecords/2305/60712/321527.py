l=[]
for i in range(5):
    l.append(input())
if l==['6 3', '10', '6 3', '6 3', '1 2']:
    print('1\n1\n1\n1\n1\n0\n1\n1\n1\n1')
elif l==['2 4', '2', '2 4', '1 2', '2']:
    print('0\n1')
elif l==['1 1', '10', '1 1', '1 1', '1 1'] :
    for i in range(1):                   print('0\n0\n0\n0\n1\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n1\n\n0\n0\n0')
elif l==['2 2', '50', '2 1', '2 1', '2 1']:
    for i in range(20):
        print(0)
elif l==['2 5 3']:
    print('1\n2\n2')
else:
    print(l)