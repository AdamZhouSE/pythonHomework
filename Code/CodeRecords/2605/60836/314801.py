"""
如题，一开始有N个小根堆，每个堆包含且仅包含一个数。接下来需要支持两种操作：
操作1： 1 x y 将第x个数和第y个数所在的小根堆合并（若第x或第y个数已经被删除或第x和第y个数在用一个堆内，则无视此操作）
操作2： 2 x 输出第x个数所在的堆最小数，并将其删除（若第x个数已经被删除，则输出-1并无视删除操作）
"""

NM=[int(m) for m in str(input()).split(" ")]
M=NM[1]

arr=[int(m) for m in str(input()).split(" ")]
position=[int(-1) for m in range(len(arr))]

instruction=[]
for i in range(M):
    instruction.append([int(m) for m in str(input()).split(" ")])

merge=[]
for i in range(M):
    tag=0
    if(instruction[i][0]==1):
        x = int(instruction[i][1]) - 1
        y = int(instruction[i][2]) - 1
        if(position[x]==-1 and position[y]==-1):
            picked = []
            picked.append(arr[x])
            picked.append(arr[y])
            merge.append(picked)
            position[x] = tag
            position[y] = tag
            tag += 1
        elif(position[x]==-1 and position[y]>=0):
            position[x]=position[y]
            merge[position[x]].append(arr[x])
        elif(position[x]>=0 and position[y]==-1):
            position[y] = position[x]
            merge[position[y]].append(arr[y])
        elif(position[x]>=0 and position[y]>=0 and position[x]!=position[y]):
            position[x]=min(position[x],position[y])
            position[y]=min(position[x],position[y])
    else:
        x = int(instruction[i][1]) - 1
        if(position[x]==-1):
            position[x]=-2
            print(arr[x])
        elif(position[x]==-2):
            print(-1)
        else:
            m = min(merge[position[x]])
            print(m)
            del merge[position[x]][merge[position[x]].index(m)]
            position[arr.index(m)] = -2