n=int(input())
s=input()
st=list(s)
for i in range(0,n):
    temp=list(map(str,input().split(" ")))
    if temp[0]=='1':
        l=list(temp[1])
        st.extend(l)
        print("".join(st))
    elif temp[0]=='2':
        a=int(temp[1])
        b=int(temp[2])
        st=st[a:a+b]
        print("".join(st))
    elif temp[0]=='3':
        a=int(temp[1])
        leng=len(st)
        st=st[0:a]+list(temp[2])+st[a:leng]
        print("".join(st))
    else:
        s="".join(st)
        if temp[1] in s:
            print(s.index(temp[1]))
        else:
            print(-1)