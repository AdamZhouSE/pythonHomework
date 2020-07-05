n = int(input())
s = ''
for i in range(n):
    cin = input().split(' ')
    if cin[0] == 'T':
        s += cin[1]
    elif cin[0] == 'Q':
        print(s[int(cin[1])-1])
    else:
        s = s[:len(s)-int(cin[1])]