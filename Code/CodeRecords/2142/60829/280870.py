n=int(input())
for p in range(n):
    s=str(input())
    ss=""
    count=0
    for i in range(0,len(s)):
        if s[i]=="(":
            count += 1
            ss=ss+str(count)+" "
        elif s[i]==")":
            ss=ss+str(count)+" "
            count -= 1
    print(ss)