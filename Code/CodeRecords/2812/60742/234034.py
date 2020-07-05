n = int(input())
l = input().split()
s = set(l)
if "0" in s:
    ways = len(s)-1
else:
    ways = len(s)
print (ways)