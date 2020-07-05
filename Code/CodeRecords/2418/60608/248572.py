def func16():
    tomatoSlices = eval(input())
    cheeseSlices = eval(input())
    res = []
    for big in range(0, cheeseSlices + 1):
        if 4 * big + 2 * (cheeseSlices - big) == tomatoSlices:
            res = [big, cheeseSlices - big]
            break
    print(res)
func16()