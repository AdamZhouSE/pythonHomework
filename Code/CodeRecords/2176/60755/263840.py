string = input()
res = []
for i in range(1,len(string)+1):
    res.append(string[-i:])
res.sort()
s = ""
for i in res:
    s = s + str(len(string)-len(i)+1)+" "
print(s[:-1])