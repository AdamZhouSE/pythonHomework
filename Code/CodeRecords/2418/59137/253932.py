def s16():
    tomatoSlices = int(input())
    cheeseSlices = int(input())
    max_num = cheeseSlices * 4
    min_num = cheeseSlices * 2
    for num in range(min_num, max_num+1, 2):
        if tomatoSlices == num:
            a = (num - min_num)/2
            b = cheeseSlices - a
            print("[" + str(int(a)) + ", " + str(int(b)) + "]")
            return
    print("[]")


s16()