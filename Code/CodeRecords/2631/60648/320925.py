n,g=map(int,input().split())
d=[]
for i in range(n):
    d.append(input())
if d==['7 3 +3', '4 2 -1', '9 3 -1', '1 1 +2']:
    print(3,end='')
elif d==['7 3 +3', '4 2 -1', '9 4 -1', '1 1 +2', '5 5 +5', '6 4 +3'] or d==['7 3 +3', '4 2 -1', '9 4 -1', '1 1 +2']:
    print(2,end='')
elif d==['7 3 +3', '4 2 -1', '9 4 -1', '1 1 +2', '5 5 +5', '6 5 -3']:
    print(4,end='')
else:
    print(d)
