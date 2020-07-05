n=int(input())
for k in range(0,n):
    str=input()
    if len(str)>26:
        print("0")
    else:
        flag=False
        for i in range(0,len(str)-1):
            if flag:
                break
            for j in range(i+1,len(str)):
                if flag:
                    break
                if str[i]==str[j]:
                    flag=True
        if flag:
            print("0")
        else :
            print("1")
                