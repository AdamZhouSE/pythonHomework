#15
ori = input().split(" ")
n = int(ori[0])#数组a大小
m = int(ori[1])#数组b大小
oriA = input().split(" ")
A = []
for i in range(0,n):
    A.append(int(oriA[i]))
oriB = input().split(" ")
B = []
for i in range(0,m):
    B.append(int(oriB[i]))
for i in range(0,m-1):
    tar = B[i]
    count = 0
    for j in range(0,n):
        if A[j] <= tar:
            count+=1
    print(count,end=" ")
tar = B[m-1]
count = 0
for j in range(0,n):
    if A[j] <= tar:
        count+=1
print(count)