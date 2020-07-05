s=input()
s=", "+s[1:len(s)-1]
ls=s.split("]")
del ls[len(ls)-1]

for i in range(len(ls)):
    ls[i]=ls[i][3:]
print(ls[len(ls)-1])