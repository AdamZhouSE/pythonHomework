n=int(input())
s=input()
for i in range(0,n):
    s1=input()
    if s1[0]=="1":
        s=s+s1[2:]
        print(s)
    elif s1[0]=="2":
        list1=list(map(int,s1.split(" ")))
        n1=int(list1[1])
        n2=int(list1[2])
        s=s[n1:n1+n2]
        print(s)
    elif s1[0]=="3":
        list1=list(s1.split(" "))
        n1=int(list1[1])
        s2=list1[2]
        s=s[0:n1]+s2+s[n1:]
        print(s)
    else:
        s2=s1[2:]
        count=0
        for i in range(0,len(s)-len(s2)+1):
            flag=True
            for j in range(0,len(s2)):
                if s[i+j]!=s2[j]:
                    flag=False
                    break
            if flag:
                count=i
                break
        print(count)
                