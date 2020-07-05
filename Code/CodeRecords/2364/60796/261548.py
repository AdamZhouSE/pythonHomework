N=int(input())
r=0
for i in range(1,N+1):
    st=str(i)
    for j in range(len(st)):
        if st.count(st[j])>1:
            r=r+1
            break
print(r)            