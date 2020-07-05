tests = int(input())
M,K = 0,0
A = []
B = []

pre = []
for i in range(tests):
    arr = list(map(int, input().split()))
    #print(arr)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in range(B.__len__()):
        A.append(B[i])
    A.sort()
    A.append(arr[2])
    pre.append(A)
#print(pre)

for i in range(pre.__len__()):
    key = int(pre[i][pre[i].__len__()-1])
    arr1 = pre[i][0:pre[i].__len__()-1]
    #print(key)
    print(arr1[key-1])