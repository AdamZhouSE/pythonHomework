arr_size=list(map(int,input().split()))
k_m=list(map(int,input().split()))
k=k_m[0]
m=k_m[1]
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
x=A[k-1]
B.sort(reverse=True)
y=B[m-1]
if x<y:
    print("YES",end="")
else:
    print("NO",end='')

