n = int(input())
arr = [int(x) for x in input().split(" ")]

setArr = set(arr)

for num in setArr:
    while arr.count(num) != 1:
        arr.remove(num)

print(len(setArr))

i = 0
while i < len(setArr):
    print(str(arr[i]), end="", flush=True)
    if i != len(setArr) - 1:
        print(" ", end="", flush=True)
    i += 1
print()
