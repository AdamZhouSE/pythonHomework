T = int(input())


def judgeTime(str1, str2):
    hour1 = int(str1[0:2])
    hour2 = int(str2[0:2])
    min1 = int(str1[2:4])
    min2 = int(str2[2:4])

    if hour1 > hour2:
        return False
    if hour1 < hour2:
        return True
    if hour1 == hour2:
        if min1 > min2:
            return False
        if min1 <= min2:
            return True


for i in range(0, T):
    length = int(input())
    temp1 = list(input().split(" "))
    temp2 = list(input().split(" "))
    lists = []
    res = []
    plats = 0

    for i in range(0, length):
        lists.append([temp1[i], temp2[i]])

    for j in range(0, length):
        res.append(lists[j])
        k=0
        while k<len(res)-1:
            if judgeTime(res[k][1], res[len(res)-1][0]):
                res.remove(res[k])
                k=k-1
            k=k+1

        plats = max(plats, len(res))

    print(plats)