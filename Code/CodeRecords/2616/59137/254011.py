def s20():
    num = int(input())
    for i in range(num):
        li = input().split()
        a = int(li[0])
        b = int(li[1])
        if a < (b * (b+1))/2:
            print("0")
        else:
            print("1")


s20()