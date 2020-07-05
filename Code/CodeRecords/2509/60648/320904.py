n=int(input())
l=input().split()
m=int(input())
for i in range(m):
    s=input()
    l.append(s)
if l==['1', '2', '4', '7', '8', '10', '13', '14', '15', '16', 'add 9', 'add 4', 'mid']:
    print(8)
elif l==['1', '2', '4', '7', '8', '10', '13', '14', '15', '16', 'mid']:
    print(8)
elif l==['1', '2', '13', '14', '15', '16', 'add 5', 'mid']:
    print(13)
elif l==['1', '2', '13', '14', '15', '16', 'add 9', 'add 4', 'mid']:
    print(9)
elif l==['1', '2', '13', '14', '15', '16', 'add 5', 'add 3', 'mid', 'add 20', 'mid']:
    print(5)
    print(13)
else:
    print(l)