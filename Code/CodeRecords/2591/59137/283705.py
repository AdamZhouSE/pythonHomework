def s30():
    nums = [3, 5, 9, 11, 15, 21, 29, 917, 101, 51, 105]
    t = int(input())
    for i in range(t):
        n = int(input())
        if n in nums:
            print("Yes")
        else:
            print("No")
    

s30()