n = int(input())
s = set(input().split())
if '0' in s and not len(s)==0:
    print(len(s)-1)
else:
    print(len(s))

