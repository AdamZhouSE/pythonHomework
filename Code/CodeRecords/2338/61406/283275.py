T = int(input())
for a in range(0,T):
    row1 = input().split(' ')
    N = int(row1[0])
    X = int(row1[1])
    array = input().split(' ')
    flag = False
    for i in range(0,N):
        for j in range(i+1,N):
            if int(array[i])+int(array[j])==X:
                flag = True
                break
        if flag:
            break
    if flag:
        print("Yes")
    else:
        print("No")