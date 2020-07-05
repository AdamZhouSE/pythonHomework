A=str(input()).split("+");
A[1]=A[1][:len(A[1])-1];
a1=int(A[0]);
b1=int(A[1]);

B=str(input()).split("+");
B[1]=B[1][:len(B[1])-1];
a2=int(B[0]);
b2=int(B[1]);
print((a1*a2-b1*b2),end="");
print("+",end="");
print(a1*b2+a2*b1,end="");
print("i");