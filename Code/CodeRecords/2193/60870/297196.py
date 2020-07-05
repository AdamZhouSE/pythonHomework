def maxSame(check_list):
    list_valid = []
    for i in range(len(check_list) - 1):
        for j in range(i + 1, len(check_list)):
            size = 0
            for k in range(0, min(len(check_list[i]), len(check_list[j]))):
                if check_list[i][len(check_list[i]) - k - 1] == check_list[j][len(check_list[j]) - k - 1]:
                    size = size + 1
                else:
                    break
            list_valid.append(size)
    return max(list_valid)


info = input().split()
size = int(info[0])
times = int(info[1])
history = input()
prefix_list = []
for i in range(1, len(history) + 1):
    prefix_list.append(history[0:i])
ask_list = []
for i in range(times):
    ask = input().split()
    ask = [int(x) for x in ask]
    ask_list.append(ask)
for i in range(times):
    ask = ask_list[i]
    front = ask[0]
    back = ask[1]
    check_list = []
    for j in range(front, back + 1):
        check_list.append(history[0:j])
    print(maxSame(check_list))