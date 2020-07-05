from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    length=int(input().strip())
    s=[int(x) for x in input().strip().split()]
    for j in range(0,len(s)-1):
        s[j]^=s[j+1]
    print(' '.join([str(x) for x in s]))