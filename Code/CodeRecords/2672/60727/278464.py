num = eval(input())
for i in range(0, num):
    number = eval(input())
    arr = list(str(bin(number))[2:])
    while len(arr) < 32: #补位
        arr.insert(0, "0")
    for i in range(0, len(arr)):
        if arr[i] == "1":
            arr[i] = "0"
        else:
            arr[i] = "1"
    print(int("".join(arr), 2))