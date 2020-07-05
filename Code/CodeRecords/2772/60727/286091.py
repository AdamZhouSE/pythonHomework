for i in range(0,eval(input())):
    num = eval(input())
    for j in range(0,100):
        if pow(j,3)==num:
            print(j)
            break
        if pow(j,3)>num:
            print(j-1)
            break