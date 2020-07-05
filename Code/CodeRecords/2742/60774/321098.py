import copy

n = int(input())
ver = [[]]
for i in range(0,n):
    op = input().split()
    v = int(op[0])
    mode = int(op[1])
    num = int(op[2])
    temp = copy.deepcopy(ver[v])
    if(mode == 1):
        temp.append(num)
        temp.sort()
    elif(mode == 2):
        if(num in temp):
            temp.remove(num)
    elif(mode == 3):
        k = temp.index(num)
        print(k + 1)
    elif(mode == 4):
        print(temp[num - 1])
    elif(mode == 5):
        lst = list(filter(lambda x: x < num,temp))
        if(lst == []):
            print(-2147483647)
        else:
            print(lst[-1])
    elif(mode == 6):
        lst = list(filter(lambda x: x > num,temp))
        if(lst == []):
            print(2147483648)
        else:
            print(lst[-1])
    ver.append(temp)