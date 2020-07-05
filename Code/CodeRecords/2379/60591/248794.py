def run(string):
    # 上 左 下 右
    directions = [[0,1],[-1,0],[0,-1],[1,0]]
    path = [[0,0]]
    now = [0,0]
    direction = 0
    for x in range(4):
        for m in range(len(string)):
            if(string[m] == 'G'):
                temp = [now[0] + directions[direction][0],now[1] + directions[direction][1]]
                now = temp
                path.append(temp)
            elif(string[m] == 'R'):
                direction += 1
            elif(string[m] == 'L'):
                direction -= 1
                if(direction == -1):
                    direction = 3
        if([0,0] == path[-1]):
            return True
    return False

print(run(input()))