num = int(input())
for i in range(num):
    arr = list(input())
    count = 0
    l = 0
    for ch in arr:
        if ch == "(":
            l += 1
        else:
            if l > 0:
                l -= 1
                count += 2
    print(count)
