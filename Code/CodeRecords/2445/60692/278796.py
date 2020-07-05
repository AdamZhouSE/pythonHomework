s = input().split(", ")
s = [list(i[5:-1]) for i in s]
s[0].sort()
s[1].sort()
if s[0] == s[1]:
    print("true")
else:
    print("false")