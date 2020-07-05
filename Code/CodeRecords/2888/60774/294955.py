s = input().split(' ')
n = int(s[0])
m = int(s[1])
numLst = list(map(int,input().split(' ')))
for i in range(0,m):
    s = input().split(' ')
    l = int(s[0])
    r = int(s[1])
    print((l - r) % 2)
        