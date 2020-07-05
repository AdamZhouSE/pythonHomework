str = input().split("\"")
s = str[1]
t = str[3]
judge = True
if len(s) != len(t):
    judge = False
for i in set(s):
    if s.count(i) != t.count(i):
        judge = False
if judge:
    print("true")
else:
    print("false")