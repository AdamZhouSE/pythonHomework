times = int(input())


def check(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True

for i in range(times):
    temp = input().split(" ")
    l = int(temp[0])
    r = int(temp[1])
    ans = 0
    for j in range(l, r + 1):
        binary = bin(j).replace("0b", "")
        count = 0
        for s in binary:
            if s == "1":
                count += 1
        if check(count):
            ans += 1
    print(ans)
