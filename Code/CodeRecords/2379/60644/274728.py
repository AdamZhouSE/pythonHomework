instruction=list(input())
arr=[[0]*100]*100
p=True
direction='north'
location=[0,0]
arr[0][0]=1
for i in range(0,len(instruction)):
    if instruction[i]=='G':
        if direction=='north':
            arr[location[0]][location[1]+1]=1
            location=[location[0],location[1]+1]
        elif direction=='sorth':
            arr[location[0]][location[1] - 1] = 1
            location = [location[0], location[1] - 1]
        elif direction=='east':
            arr[location[0]+1][location[1] ] = 1
            location = [location[0]+1, location[1] ]
        else:
            arr[location[0]-1][location[1]] = 1
            location = [location[0]-1, location[1]]
    elif instruction[i]=='L':
        if direction=='north':
            direction='west'
        elif direction=='south':
            direction='east'
        elif direction=='east':
            direction='north'
        else:
            direction='south'
    else:
        if direction=='north':
            direction='east'
        elif direction=='south':
            direction='west'
        elif direction=='east':
            direction='south'
        else:
            direction='north'
for i in range(0,5):
    for i in range(0, len(instruction)):
        if instruction[i] == 'G':
            if direction == 'north':
                if arr[location[0]][location[1] + 1] == 1:
                    p=False
                    break
                else:
                    arr[location[0]][location[1] + 1] = 1
                    location = [location[0], location[1] + 1]
            elif direction == 'sorth':
                if arr[location[0]][location[1] - 1] == 1:
                    p=False
                    break
                else:
                    arr[location[0]][location[1] - 1] = 1
                    location = [location[0], location[1] - 1]
            elif direction == 'east':
                if arr[location[0] + 1][location[1]] == 1:
                    p=False
                    break
                else:
                    arr[location[0] + 1][location[1]] = 1
                    location = [location[0] + 1, location[1]]
            else:
                if arr[location[0] - 1][location[1]] == 1:
                    p=False
                    break
                else:
                    arr[location[0] - 1][location[1]] = 1
                    location = [location[0] - 1, location[1]]
        elif instruction[i] == 'L':
            if direction == 'north':
                direction = 'west'
            elif direction == 'south':
                direction = 'east'
            elif direction == 'east':
                direction = 'north'
            else:
                direction = 'south'
        else:
            if direction == 'north':
                direction = 'east'
            elif direction == 'south':
                direction = 'west'
            elif direction == 'east':
                direction = 'south'
            else:
                direction = 'north'
    if not p:
        break
if p:
    print('False')
else:
    print('True')

