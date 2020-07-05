n = int(input())
l = input().split()
s = set(l)
if "0" in s:
    steps = len(s)-1
else:
    steps = len(s)
print (steps)