a=input()
a=a.replace(" ","")
if a[0] =='-' or  (a[0]<=chr(58) and a[0]>=chr(48)):
    list=[]
    list.append(a[0])
    for i in range(1,len(a)):
        if a[i]<=chr(57) and a[i]>=chr(48):
            list.append(a[i])
        else:
            break
    a=int("".join(list))
    if a<-2147483648:
        print(-2147483648)
    elif a>4294967295:
        print(4294967295)
    else:
        print(a)
else:
    print(0)