array = input().split(",")
array = [int(x) for x in array]
target = int(input())
sentinel = 0
for i in range(len(array)):
    if array[i] == target:
        sentinel = 1
        print(i)
        break
if sentinel == 0:
    print(-1)
