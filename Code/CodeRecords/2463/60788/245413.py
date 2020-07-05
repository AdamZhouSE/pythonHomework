import sys
s=[int(x) for x in input().split(',')]
t=int(input())
for i in range(0,len(s)-1):
    for j in range(i+1,len(s)):
        if s[i]+s[j]==t:
            print([i+1,j+1])
            sys.exit(0)
print('None')