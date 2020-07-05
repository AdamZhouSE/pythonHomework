s = input()[1:-1].split(", ")
flag = False
res = len(s);
for i in range(len(s)):
    s[i] = int(s[i])
for i in range(1,len(s)):
    for k in range(len(s)-i+1):
        temp = s.copy()
        temp.sort()
        min = s[k:k+i];
        min.sort()
        if temp==(s[:k]+min+s[k+i:]):
            res = i;
            flag = True
            break
    if flag:
        break
print(res)