array = input().split(",")
array = [int(x) for x in array]
sentinel = 0
if array[0]>array[1]:
    print(0)
    sentinel = 1
for i in range(1,len(array)-1):
    if array[i]>array[i-1] and array[i] >array[i+1]:
        print(i)
        sentinel = 1
        break
if array[-1] > array[-2] and sentinel == 0:
    print(len(array)-1)
