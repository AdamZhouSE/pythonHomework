def func19():
    t = int(input())
    while t > 0:
        t -= 1
        temp = list(map(int, input().strip().split(" ")))
        print(temp[1]-1-temp[0])
    return 
func19()