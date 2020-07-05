a = input()
a = a[5:]
s = a[:a.find('"')]
a = a[a.find('"') + 8:]
t = a[:a.find('"')]
if sorted(s) == sorted(t): print("true")
else: print("false")