numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
res = []


def solve(s):
    s = str(s)
    for i in range(10):
        j = 0
        flag = True
        while j < len(numbers[i]):
            if not s.__contains__(numbers[i][j]):
                flag = False
                break
            j += 1
        if flag:
            res.append(i)


if __name__ == '__main__':
    s = input()
    solve(s)
    res.sort()
    for i in range(len(res)):
        print(res[i],end='')
    print()