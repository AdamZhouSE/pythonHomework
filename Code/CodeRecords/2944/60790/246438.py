str1=input()
list1=[]
leng=len(str1)
j=True
for i in range(0,leng-1):
    if(str1[i]!="(" and str1[i]!=")"):
        continue
    else:
        if(str1[i]=="("):
            list1.append("(")
        else:
            if(list1[-1]=="("):
                del list1[-1]
            else:
                j=False
                break
if(len(list1)!=0):
    j=False
if(j):
    print("YES",end="")
else:
    print("NO",end="")