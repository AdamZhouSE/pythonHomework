def func13():
    t = int(input())
    while t>0:
        t -= 1
        temp = list(map(int, input().strip().split(" ")))
        if temp[0] < sum(range(1,temp[1]+1)):
            print(0)
        else:
            print(1)
    return
func13()