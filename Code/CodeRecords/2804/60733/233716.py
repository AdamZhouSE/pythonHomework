str=input()
s=str.split('+')
s.sort()
res=""
for item in s:
    res=res+item+'+'
res=res.rstrip('+')
print(res)