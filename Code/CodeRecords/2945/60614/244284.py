str=input()
boy=0
girl=0
i=0
while i<len(str):
    if str[i] in "boy":
        boy+=1
        if i<len(str)-2:
            if str[i]+str[i+1]+str[i+2]=="boy":
                i+=2
            elif str[i]+str[i+1] in "boy":
                i+=1
        elif i==len(str)-2:
            if str[i]+str[i+1] in "boy":
                i+=1
    if str[i] in "girl":
        girl+=1
        if i<len(str)-1:
            if str[i]+str[i+1] in "girl":
                i+=1
                if i<len(str)-1:
                    if str[i-1] + str[i] + str[i+1] in "girl":
                        i+=1
                    if i<len(str)-1:
                        if str[i-2] + str[i-1] + str[i]+str[i+1]=="girl":
                            i += 1
    i+=1
print(boy)
print(girl,end="")