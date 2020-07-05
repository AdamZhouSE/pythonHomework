t = int(input())
for test in range (t):
    n,m =map(int, input().split())
    people = list(range(1, n + 1))

    index = 0
    res = []

    # 给n个人编号放到表people中,从下标为0的人开始

    for i in range(n):

        # for循环用来控制内部循环执行次数

        count = 0

        while count < m:

            if people[index] != 0:
                count += 1

            if count == m:
                res.append(people[index] - 1)

                # 把退出的人的编号置0

                people[index] = 0

            index = (index + 1) % n
    for i in range(len(res)):
        if res[i]==0:
            print(i+1)

