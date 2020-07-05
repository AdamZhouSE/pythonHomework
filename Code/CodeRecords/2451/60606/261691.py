array = input().split(",")
array = [int(x) for x in array]
target = int(input())
sentinel = 0
for i in range(len(array)):
    if array[i] >= target:
        print(i)
        sentinel = 1
        break
if sentinel == 0:
    print(len(array))
    
