n = int(input())
s = input()
for i in range(n):
    a = input().split(' ')
    left = 0
    if a[0] == '1':
        s += a[1]
    if a[0] == '2':
        s = s[int(a[1]):int(a[1])+int(a[2])]
    if a[0] == '3':
        l = s[0:int(a[1])]
        s = l + a[2] + s[int(a[1]):]
    if a[0] == '4':
        t = a[1]
        print(s.find(a[1]))
    else:
        print(s)

