s=input()
s=s[1:len(s)-1]
sl=s.split(',')
#print(sl)
re=[]
for i in sl:
    re.append(i)
re2=[]
for i in re:
    if(i[0:1]=='['):
        i=i[1:]
    elif i[len(i)-1:len(i)]==']':
        i=i[0:len(i)-1]
    re2.append(int(i))
re2.sort()
print(re2)