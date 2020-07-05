num=int(input())
for k in range(num):
    s=input()
    #print(s)
    n=[]
    for i in range(len(s)):
        #print(n)
        if s[i]>='0' and s[i]<='9':
            n.append(int(s[i]))
        elif s[i]=='+':
            n1=n[len(n)-1]
            n2=n[len(n)-2]
            n3=n1+n2
            n=n[:len(n)-2]
            #print(n3)
            n.append(n3)
        elif s[i]=='-':
            n1=n[len(n)-1]
            n2=n[len(n)-2]
            n3=n2-n1
            n=n[:len(n)-2]
            #print(n3)
            n.append(n3)
        elif s[i]=='*':
            n1=n[len(n)-1]
            n2=n[len(n)-2]
            n3=n1*n2
            n=n[:len(n)-2]
            #print(n3)
            n.append(n3)
        elif s[i]=='/':
            n1=n[len(n)-1]
            n2=n[len(n)-2]
            n3=n2//n1
            n=n[:len(n)-2]
            #print(n3)
            n.append(n3)
        else:
            pass
    print(n[0])
            