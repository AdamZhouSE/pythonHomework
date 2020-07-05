def bubble(ls):
    
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-i-1:
            if ls[j][0]>ls[j+1][1] or(ls[j][0]==ls[j+1][0] and ls[j][1]>ls[j+1][1]):
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1

    return ls
s=input()
s=", "+s[1:len(s)-1]
ls=s.split("]")
del ls[len(ls)-1]

for i in range(len(ls)):
    ls[i]=ls[i][3:]
    ls[i]=ls[i].split(",")
ls=bubble(ls)
s="["+ls[len(ls)-1][0]+", "+ls[len(ls)-1][1]+"]"
print(s)