s = input()
s = s.replace(" ","")
num = ""
if(s[0].isdigit() == False and s[0]!="-"):
    print(0)
elif(s[0] == "-"):
    num += "-"
    for i in range(1,len(s)):
        if(s[i].isdigit()):
            num += s[i]
        else:
            break
    if(len(num)>11 or (len(num)==11 and num[1]>2)):
        print("-2147483648")
    else:
        print(num)
else:
    for i in range(0,len(s)):
        if (s[i].isdigit()):
            num += s[i]
        else:
            break
    if (len(num) > 10 or (len(num) == 10 and num[1] > 2)):
        print("2147483648")
    else:
        print(num)