str=input()
list=[]
for i in range(len(str)):
    if str[i]!=")":
        list.append(str[i])
    else:
        while list[-1]!="(":
            list.pop(-1)
        list.pop(-1)

if "(" not in list and ")" not in list:
    print("YES",end="")
else:
    print("NO",end="")