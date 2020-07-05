array = input().split(",")
array.reverse()
array = [int(x) for x in array]
for i in range(len(array)-1):
    if array[i] >= i+1 and array[i+1] <= i+1:
        print(i+1)
        break