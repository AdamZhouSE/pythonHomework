nums = int(input())
orzFang_list = input().split()
next_list = input().split()
orzFang_list = [int(x) for x in orzFang_list]
next_list = [int(x) for x in next_list]
for i in range(len(next_list)):
    circle_list = [i]
    res = orzFang_list[i]
    start = i
    while next_list[start] - 1 not in circle_list:
        start = next_list[start] - 1
        res = res + orzFang_list[start]
        circle_list.append(start)
    print(res)