k=input()
for j in range(int(k)):
    a=eval(input())
    b=[-1 for i in range(a)]
    i=-1
    index=1
    while index<=a:
        t=0
        i+=1
        while b[i%a]!=-1:
            i+=1
        while t<index:
            t+=1
            i+=1
            while b[i % a] != -1:
                i += 1
        b[i%a]=index
        index+=1



    st=""
    for k in b:
        st+=str(k)
        st+=" "

    print(st.rstrip())