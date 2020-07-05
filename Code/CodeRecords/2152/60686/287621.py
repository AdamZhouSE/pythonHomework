def calcu(list1, list2, begin, sums):
    if res_temp.count(list2[begin - 1]) != 0:
        return sums
    else:
        res_temp.append(list2[begin - 1])
        sums += list1[list2[begin - 1] - 1]
        return calcu(list1, list2, list2[begin - 1], sums)


nums = int(input())
fang_num = input().split(" ")
dis = input().split(" ")
for i in range(len(fang_num)):
    fang_num[i] = int(fang_num[i])
for i in range(len(dis)):
    dis[i] = int(dis[i])
for i in range(nums):
    res_temp = [i+1]
    sum_total = fang_num[i]
    print(calcu(fang_num, dis, i+1, sum_total))
