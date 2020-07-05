s = input()
t = input()
result = True
k = 0
for i in range(len(s)):
    temp = t[k:]
    k = t.find(s[i])
    if k==-1:   
        result = False
        break
print(result)