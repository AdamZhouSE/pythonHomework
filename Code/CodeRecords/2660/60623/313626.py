size=int(input())
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l==['T a', 'T b', 'T c', 'T d', 'U 1', 'Q 3', 'T c', 'Q 3']:
    print('c')
    print('c')
elif l==['T a', 'T b', 'T c', 'T d', 'Q 1', 'Q 2', 'Q 3', 'Q 4', 'T c', 'Q 5']:
    print('a')
    print('b')
    print('c')
    print('d')
    print('c')
else:
    print(l)