n = int(input())
s = set()
l = len(s)
for i in range(n):
    s.add(input())
    if len(s)==l :
        print('YES')
    else:
        print('NO')
    l = len(s)
   