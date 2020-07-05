def func23():
    t = int(input())
    while t > 0:
        t -= 1
        temp = list(map(int, input().strip().split(" ")))
        print(pow(2,temp[1])-temp[0])
    return
func23()