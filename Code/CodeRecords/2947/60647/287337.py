n=int(input())
str=input()
for i in range(n):
    list=input().split()
    if list[0]=='1':
        str=str+list[1]
        print(str)
    elif list[0]=='2':
        a=int(list[1])
        b=int(list[2])
        res=''
        for j in range(a,a+b):
            res=res+str[j]
        str=res
        print(res)
    elif list[0]=='3':
        res=''
        a = int(list[1])
        for j in range(a):
            res=res+str[j]
        res=res+list[2]
        for j in range(a,len(str)):
            res = res + str[j]
        str=res
        print(res)
    else:
        str1=list[1]
        b=0
        for j in range(len(str)):
            if str[j]==str1[0]:
                a=0
                for k in range(j,j+len(str1)):
                    if str[k]!=str1[k-j]:
                        a=1
                        break
                if a==0:
                    b=1
                    print(j)
                    break
        if b==0:
            print('-1')