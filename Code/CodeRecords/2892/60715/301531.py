M,N=input().split()
M=int(M)
N=int(N)
if(M>N):
    print("0 0 0 0 0 0 0 0 0 0")
else:
    st=""
    while M<=N:
        st+=str(M)
        M+=1
    i=0
    while i<10:
        print(st.count(str(i)),end=" ")
        i+=1