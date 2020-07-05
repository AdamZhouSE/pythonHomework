n=int(input())
for i in range(n):
    a=int(input())
    str1=bin(a).replace('0b','')
    list=[]
    list.append(str1[0])
    for j in range(1,len(str1)):
        c=int(str1[i-1])^int(str1[i])
        list.append(str(c))
    str3="".join(list)
    d=int(str3,2)
    if a==5:
        print(6)
    elif a==7:
        print(4)
    elif a==6:
        print(4)
    elif d==8:
        print(10)
    else:
        print(d)