s=input()
a=[]
for i in range(len(s)-1):
    if s[i+1]=='+':
        a.append(int(s[i]))
a.sort()
b=[]
for aa in a:
    b.append(str(aa))
print('+'.join(b))
        
