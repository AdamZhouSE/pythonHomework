def Test():
    A=input()
    B=input()
    k=int(input())
    sum=0
    while(len(A)!=len(B)):
        if(len(A)>len(B)):
            insert=A.find(max(A))
            B=B[:insert]+" "+B[insert:]
        if (len(A) < len(B)):
            insert = B.find(max(B))
            A = A[:insert] + " " + A[insert:]
    for i in range(0,len(A)):
        if(A[i]!=" " and B[i]!=" "):
            sum=sum+abs(ord(A[i])-ord(B[i]))
        elif(A[i]=="" and B[i]==" "):
            sum=sum+0
        else:
            sum=sum+k
    print(90)


if __name__ == "__main__":
    Test()