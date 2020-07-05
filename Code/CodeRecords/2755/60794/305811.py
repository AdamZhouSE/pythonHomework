num = int(input())
for i in range(num):
    arr = input().split(" ")
    arr1 = int(arr[0])
    arr2 = int(arr[1])
    ans = [0]*(arr1+arr2-1)
    p = input().split(" ")
    one = []
    for j in range(len(p)):
        one.append(int(p[j]))
    p = input().split(" ")
    two = []
    for j in range(len(p)):
        two.append(int(p[j]))
    for j in range(len(one)):
        for k in range(len(two)):
            ans[j + k] = ans[j + k] + one[j] * two[k]
    for j in range(len(ans)-1):
        print(ans[j], end=" ")
    print(ans[len(ans)-1])