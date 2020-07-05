def find(array,x):
    for i in range(len(array)):
        if array[i] == x:
            return (i+1)
n,m =list(map(int,input().split(" ")))
array = input().strip().split(" ")
array = [int(x) for x in array]
for i in range(m):
    temp = input().strip().split(" ")
    temp = [int(x) for x in temp]
    if temp[0] == 1:
        start = temp[1]-1
        end = temp[2]
        temp2 = array[start:end].copy()
        temp2.sort()
        print(find(temp2,temp[3]))
    elif temp[0] ==2 :
        start = temp[1]-1
        end = temp[2]
        temp2 = array[start:end].copy()
        temp2.sort()
        print( temp2[temp[3]-1])
    elif temp[0] == 3:
        pos = temp[1] - 1
        x = temp[2]
        array[pos] = x
    elif temp[0] ==4:
        start = temp[1] - 1
        end = temp[2]
        temp2 = array[start:end].copy()
        temp2.sort()
        for j in range(len(temp2)):
            if temp2[j]>=temp[3]:
                print(temp2[j-1])
                break
    else:
        start = temp[1] - 1
        end = temp[2]
        temp2 = array[start:end].copy()
        temp2.sort()
        for j in range(len(temp2)):
            if temp2[j]>temp[3]:
                print(temp2[j])
                break
