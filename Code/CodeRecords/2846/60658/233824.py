n = int(input())
s = set(input().split())
print(len(s)-1 if '0' in s and not len(s)==0 else len(s) )
