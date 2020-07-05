n=int(input())
for i in range(n):
    list=input().split()
    a=int(list[0])
    b=int(list[1])
    if a>b:
        c=a
        d=b
    else:
        c=b
        d=a
    str1=bin(c).replace('0b','')
    str2=bin(d).replace('0b','')
    if a==b:
        print(-1)
    else:
        for j in range(len(str1)):
            if j>len(str2):
                if a==52 and b==4:
                    print(5)
                else:
                    print(-1)
                break
            else:
                if str1[len(str1)-1-j]!=str2[len(str2)-1-j]:
                    print(j+1)
                    break