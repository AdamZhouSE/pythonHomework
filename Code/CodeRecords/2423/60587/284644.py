T = int(input())
while T > 0:
    T -= 1
    n1, n2 = input().split(' ')
    arr1 = input().split(' ')
    arr2 = input().split(' ')
    num1 = [int(arr1[i]) for i in range(len(arr1))]
    num2 = [int(arr2[i]) for i in range(len(arr2))]
    count = 0
    for i in range(0, len(num2)):
        for j in range(0, len(num1)):
            if num2[i] == num1[j]:
                count += 1
                break
    if count == int(n2):
        print("Yes")
    else:
        print("No")
