str=input()
temp=input()
order=temp[0]
if (order=="D"):
    i=1
    while temp[i]==" ":
        i=i+1
    if temp[i] not in str:
        print("no exist")
    else:
        index=str.index(temp[i])
        str=str[0:index]+str[index+1:]
elif (order=="I"):
    j = 1
    while temp[j] == " ":
        j = j + 1
    if temp[j] not in str:
        print("no exist")
    else:
        k = j + 1
        while temp[k] == " ":
            k = k + 1
        i=len(str)-1
        while i>=0:
            if(str[i]==temp[j]):
                break
            i=i-1
        str=str[0:i]+temp[k]+str[i:]
elif (order=="R"):
    j = 1
    while temp[j] == " ":
        j = j + 1
    if temp[j] not in str:
        print("no exist")
    else:
        i=0
        while i<len(str):
            if(str[i]==temp[j]):
                k = j+1
                while temp[k] == " ":
                    k = k + 1
                str=str[0:i]+temp[k]+str[i+1:]
                i=i+1
            i=i+1
print(str)
