L, T, O = [int(x) for x in input().split()]
board = [0] * (L + 1)
ans = []
flag = False
for i in range(O):
    chars = [x for x in input().split()]
    if flag:
        print(chars)
    if chars[0] == 'C':
        begin = min(int(chars[1]), int(chars[2]))
        end = max(int(chars[1]), int(chars[2])) + 1
        C = int(chars[3])
        for j in range(begin, end):
            board[j] = C
    elif chars[0] == 'P' or chars[0] == 'p':
        begin = min(int(chars[1]), int(chars[2]))
        end = max(int(chars[1]), int(chars[2])) + 1
        color = []
        for j in range(begin, end):
            if board[j] not in color:
                color.append(board[j])
        print(len(color))
        ans.append(len(color))
        #if len(color)==2:
        #    flag = True
    #if ans==[2,2]:
    #    flag = True