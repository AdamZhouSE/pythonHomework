def pancake_sort(temp: list, move=None):
    if move is None:
        move = []
    if len(temp) == 1:
        print(move)
    else:
        index = temp.index(max(temp))
        if index != len(temp) - 1:
            if index != 0:
                move.append(index + 1)
                ans = temp[: index + 1]
                ans.reverse()
                temp[: index + 1] = ans
            move.append(len(temp))
            temp.reverse()
        temp = temp[: -1]
        pancake_sort(temp, move)


nums = eval(input())
pancake_sort(nums)
trial = [0, 1, 2, 4]
