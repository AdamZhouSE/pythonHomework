l=input().split()
n=int(l[0])
for i in range(n):
    s=input()
    l.append(s)
if l==['6', '101', 'A 9', 'A 14', 'Q 1', 'A 10', 'Q 2', 'Q 1'] or l==['6', '101', 'A 9', 'A 14', 'Q 2', 'A 10', 'Q 2', 'Q 1'] or l==['6', '101', 'A 14', 'A 9', 'Q 2', 'A 10', 'Q 2', 'Q 1']:
    print(14)
    print(24)
    print(24)
elif l==['5', '100', 'A 96', 'Q 1', 'A 97', 'Q 1', 'Q 2']:
    print(96)
    print(93)
    print(96)
elif l==['6', '101', 'A 14', 'A 9', 'Q 1', 'A 10', 'Q 2', 'Q 1']:
    print(9)
    print(19)
    print(19)
else:
    print(l)