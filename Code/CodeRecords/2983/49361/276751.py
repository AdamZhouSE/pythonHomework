n = int(input())
sequence = input()


def judge(x):
    answer = 0
    copy = list(x[:])
    if len(copy) % 2 == 0:
        while (copy):
            tmp = copy.pop(0)
            if tmp not in copy:
                print('Impossible')
                return 0
            else:
                copy_1 = copy[::-1]
                i = copy_1.index(tmp)
                answer += i
                copy_1.remove(tmp)
                copy = copy_1[::-1]
        print(answer)
        return 1
    else:
        flag = 0
        cnt = 0
        while (copy):
            tmp = copy.pop(0)
            if tmp not in copy:
                cnt += 1
                flag = 1
                if (cnt == 2):
                    print('Impossible')
                    return 0
            else:
                copy_1 = copy[::-1]
                i = copy_1.index(tmp)
                if flag == 1:
                    answer += i + 1
                else:
                    answer += i
                copy_1.remove(tmp)
                copy = copy_1[::-1]
        print(answer)
        return 1


judge(sequence)
