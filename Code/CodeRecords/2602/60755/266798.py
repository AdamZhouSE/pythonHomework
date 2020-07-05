s1 = input()[1:-1].replace(",","")
s2 = input()[1:-1].replace(",","")
if len(s2)>len(s1):
    temp = s1
    s1 = s2
    s2 = temp
res = []
for i in range(1,len(s2)+1):
    for k in range(len(s2)-i+1):
        for m in range(len(s1)-i+1):
            if s2[k:k+i]==s1[m:m+i]:
                res.append(i)
res.sort()
print(res[-1])
    