s=input()
length=len(s)
temp=[]
for i in range(0,length):
    temp.append(s[i:])
temp.sort()
re=[]
for i in temp:
    re.append(str(length-len(i)+1))
print(" ".join(re))