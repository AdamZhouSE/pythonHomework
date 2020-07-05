array = input().split(",")
array = [int(x) for x in array]
target = int(input())
sentinel = 0
for num in array:
    if num == target:
        print("True")
        sentinel = 1
        break
if sentinel == 0:
    print("False")