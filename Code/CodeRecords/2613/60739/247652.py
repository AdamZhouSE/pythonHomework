def getConnell(num):
    list = [1, 2]
    ctr = 2
    while len(list) <= num:
        while list[-1] < ctr * ctr:
            list.append(list[-1] + 2)
        list.append(list[-1] + 1)
        ctr += 1

    return list[0:num]

if __name__ == '__main__':
    nums = int(input())
    for i in range (nums):
        l = int(input())
        a = getConnell(l)
        print(" ".join(str(i) for i in a))
