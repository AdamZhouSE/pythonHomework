A=input().split(",")
now = []
for index in range(len(A)):
    now.append((int)(A[index]))
max=0
zj=0
for index in range(len(now)):
    zj+=now[index]
    if zj>max:
        max=zj
    elif max+now[index]<0:
        zj=0
print(max)