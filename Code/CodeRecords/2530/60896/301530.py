str1=input()
str2=input()
res = []
for ch in str1:
    res.append(ch * str2.count(ch))
for ch in str2:
    if ch not in str1:
        res.append(ch)    
print ("".join(res))
