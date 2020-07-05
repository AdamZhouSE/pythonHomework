def question17():
    dict = {}
    num = int(input())
    step = input().split(' ')
    list = []
    for e in step:
        list.append(int(e))
    for i in list:
        if dict.keys().__contains__(i):
            dict[i] += 1
        else:
            dict[i] = 1
    keys = []
    for key in dict.keys():
        keys.append(key)
    if len(keys) <= 3:
        if len(keys) == 2:
            if abs(keys[0] - keys[1]) == 6:
                return 3
            return abs(keys[0] - keys[1])
        elif len(keys) == 1:
            return 0
        else:
            if not sum(keys) % 3 == 0:
                return -1
            else:
                return max(abs(keys[0] - sum(keys)//3),abs(keys[1] - sum(keys)//3))
    return -1

if __name__ == '__main__':
    print(question17())