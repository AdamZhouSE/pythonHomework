T = int(input())
for i in range(T):
    nk = (''+input()).split(' ')
    nums = int(nk[0])
    call = int(nk[1])
    peoples = [True for _ in range(nums)]

    # append的方法性能不好
    # for _ in range(nums):
    #    peoples.append(True)

    result = []
    num = 1

    while (any(peoples)):
        for index, people in enumerate(peoples):
            if people:
                if num == call:
                    peoples[index] = False
                    result.append(index + 1)
                    #                print(index+1)#每轮的出局者
                    #                print(peoples)#每次的队列状态
                    num = 1
                else:
                    num += 1

    print(result[nums - 1])