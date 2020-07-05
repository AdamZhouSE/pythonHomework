def A(n):
    s=""
    if n==1:
        s="A"
    else:
        s=A(n-1)+chr(ord("A")+n-1)+A(n-1)
    return s

n=int(input())
print(A(n))