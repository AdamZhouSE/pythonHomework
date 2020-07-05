num = list(input())

if(num[0]=="-"):
    num.remove("-")
    num.reverse()
    if(num[0]=="0"):
        print("-" + "".join(num[1:]))
    else:
        print("-"+"".join(num))
else:
    num.reverse()
    if (num[0] == "0"):
        print("".join(num[1:]))
    else:
        print("".join(num))