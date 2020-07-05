s=input()
s=s[1:len(s)-1]
sl=s.split(',')
re=[]
for i in sl:
    re.append(int(i))
re.sort()
print(re)