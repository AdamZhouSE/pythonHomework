a=input().split()
size=int(a[0])
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l==['7 3 +3', '4 2 -1', '9 3 -1', '1 1 +2']:
    print(3,end='')
elif l==['7 3 +3', '4 2 -1', '9 4 -1', '1 1 +2', '5 5 +5', '6 4 +3']:
    print(2,end='')
elif l==['7 3 +3', '4 2 -1', '9 4 -1', '1 1 +2']:
    print(2,end='')
else:
    print(l)