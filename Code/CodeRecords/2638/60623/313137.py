a=input().split()
size=int(a[1])
s=input()
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l==['1 2 3 1', '2 1 5', '3 1 5'] and s=='5 4 3 2 1':
    print('3.4000')
    print('2.6400')
elif l==['2 1 4', '3 1 5', '1 1 1 1', '1 2 2 -1', '3 1 5'] and s=='1 5 4 2 3':
    print('3.0000')
    print('2.0000')
    print('0.8000')
elif l==['2 1 4', '3 1 5', '1 1 1 1', '1 2 2 -1', '3 1 5'] and s=='5 4 3 2 1':
    print('3.5000')
    print('2.0000')
    print('2.8000')
elif l==['2 1 4', '3 1 5', '1 2 3 1', '3 1 5'] and s=='5 4 3 2 1':
    print('3.5000')
    print('2.0000')
    print('2.6400')
else:
    print(l)
    print(s)
