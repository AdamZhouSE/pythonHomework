l=[]
source=input()
while source!="!":
    l.append(source)
    source=input()
for i in range(len(l)):
    str=""
    for j in range(len(l[i])):
        if l[i][j].isalpha():
            if l[i][j].isupper():
                alpha=chr(ord("Z")-ord(l[i][j])+ord("A"))
            else:
                alpha = chr(ord("z") - ord(l[i][j]) + ord("a"))
            str=str+alpha
        else:
            str=str+l[i][j]
    print(str)   