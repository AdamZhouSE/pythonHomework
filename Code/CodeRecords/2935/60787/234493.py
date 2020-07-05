num=0
case=1
str=list(input())
for i in str:
    if i=="Q" or i=="A":
        if case==1:
            if i=="Q":
                case=2
        if case==2:
            if i=="A":
                case=3
            else:
                case=1
        if case==3:
            if i=="Q":
                num+=1
                case=1
print(num)