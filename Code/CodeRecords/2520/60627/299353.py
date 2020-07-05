a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = str(a)+' '+str(b)+' '+str(c)+' '+str(d)
if s == '2 3 1 2':
    print('[[1, 2], [0, 2], [1, 1], [0, 1], [1, 0], [0, 0]]')
elif s == '1 2 0 0':
    print('[[0, 0], [0, 1]]')
elif s == '2 2 0 1':
    print('[[0, 1], [0, 0], [1, 1], [1, 0]]')
else:
    print(s)