s=input()
s=", "+s[1:len(s)-1]
ls=s.split("]")
del ls[len(ls)-1]

for i in range(len(ls)):
    ls[i]=ls[i][3:]
    ls[i]=ls[i].split(",")

s="["+ls[len(ls)-1][0]+", "+ls[len(ls)-1][1]+"]"
print(s)