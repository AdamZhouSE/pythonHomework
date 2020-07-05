m = input()
a = m.find("\"")
b = m[a+1:].find("\"")+a+1
c = m[b+1:].find("\"")+b+1
d = m[c+1:].find("\"")+c+1
s = m[a+1:b]
t = m[c+1:d]
result = "true"
if len(s)!=len(t): result = "false"
for x in s:
    if s.count(x)!=t.count(x):
        result = "false"
print(result)