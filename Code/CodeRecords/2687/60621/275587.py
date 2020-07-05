a=eval(input())
for i in range(a):
    num=eval(input())
    st=""
    s=""
    flag=1
    now=0
    while now<=num:
        flag*=-1
        if flag<0:
            now=now*2+1
        else:
            now=now*2
        if now<=num:
            st+=str(now)+" "
    print(st.rstrip())