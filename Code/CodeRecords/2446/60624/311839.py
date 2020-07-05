def func8():
    n = int(input())
    temp = []
    for i in range(n):
        temp.append(input().split(" "))
    m = int(input())
    for i in range(m):
        str = input().strip()
        flag = False
        for i in range(n):
            if str in temp[i][1:]:
                print(i+1,end=" ")
                flag = True
        if not flag:
            print(" ")
        else:
            print()
    return
func8()