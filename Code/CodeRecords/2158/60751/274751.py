import math
str_=input()
a=0
for i in range(len(str_)):
    if str_[i]!=" ":
        a=i
        break
result=""
if str_[a]=="-":
    result+="-"
    for i in range(a+1,len(str_)):
        if str_[i].isdigit():
            result+=str_[i]
        else:
            break
elif str_[a].isdigit():
    for i in range(a,len(str_)):
        if str_[i].isdigit():
            result+=str_[i]
        else:
            break
else:
    result="0"

if int(result)<0-math.pow(2,31):
    print(int(0-math.pow(2,31)))
elif int(result)>math.pow(2,31)-1:
    print(int(math.pow(2,31)-1))
else:
    print(result)

