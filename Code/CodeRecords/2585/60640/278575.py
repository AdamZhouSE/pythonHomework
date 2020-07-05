def is_able_to_transfer(s, e):
    start = list(s)
    end = list(e)
    if len(start) != len(end):
        return False
    for i in range(len(start)):
        # 当出现不等的情况
        if start[i] != end[i]:
            # 最后一个元素不等，不可能转换
            if i == len(start)-1:
                return False
            if start[i] == end[i+1] == 'X' and start[i+1] == end[i] == 'L':
                temp = start[i]
                start[i] = start[i+1]
                start[i+1] = temp
            elif start[i] == end[i+1] == 'R' and start[i+1] == end[i] == 'X':
                temp = start[i]
                start[i] = start[i + 1]
                start[i + 1] = temp
            else:
                return False
    return True


inp1 = input()
inp2 = input()
print(is_able_to_transfer(inp1, inp2))
