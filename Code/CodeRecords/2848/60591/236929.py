size = input()
temp = input().split(" ")
k = eval(temp[0])
m = eval(temp[1])
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))
A.sort()
B.sort()
if(A[k-1] < B[-(m)]):
    print("YES")
else:
    print("NO")