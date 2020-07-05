def judge(arrJ):
    for k in range(0, len(arrJ)):
        if arrJ.count(arrJ[k]) * 2 > len(arrJ):
            return arrJ[k]
        else:
            continue
    return -1


num = input()
arr = []
for i in range(0, int(num)):
    nums = input()
    arr = input().split(" ")
    print(judge(arr))
