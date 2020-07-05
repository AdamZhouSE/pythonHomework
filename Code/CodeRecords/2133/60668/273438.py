def nums_21_leastC(list = []):
    moves = 0
    minN = max(list)+1
    for i in range(len(list)):
        minN = min(minN , list[i])
    for i in range(len(list)):
        moves += list[i] - minN
    print(moves)
if __name__=='__main__':
    list = [int(i) for i in input().split(',')]
    nums_21_leastC(list)