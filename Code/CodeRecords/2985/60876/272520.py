n=int(input())
st=[]
temp=[]
m=ord('C')
if n==1:
    print("A")
elif n==2:
    print("ABA")
else:
    st.extend(list("ABA"))
    temp.append("BA")
    n-=2
    for i in range(0,n):
        c=chr(i+m)+'A'
        for j in range(0,i+1):
            c+=temp[j]
        temp.append(c)
        st.extend(list(temp[i+1]))
    print("".join(st))