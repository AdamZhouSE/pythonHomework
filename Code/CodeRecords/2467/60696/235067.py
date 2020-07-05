input()
k = int(input()[-1])
arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
arr1.extend(arr2)
arr1.sort()
print(arr1[k-1])