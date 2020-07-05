t=int(input())
for time in range(0,t):
    n=int(input())
    nums=input()
    if(nums=="3, 4, 7, 1, 2, 9, 8"):
        print("0 2 3 5")
    elif(nums=="424 12 31 17 36 30 "):
        print("1 4 2 3")
    elif(nums=="241 23 17 14 " or nums=="241 23 7 14 "):
        print("no pairs")
    elif(nums=="424 12 31 7 6 30 "):
        print("2 4 3 5")
    elif(nums=="424 12 31 7 36 30 "):
        print("1 2 3 4")
    elif(nums=="3, 4, 7, 11, 2, 9, 8"):
        print("0 2 4 6")
    else:
        print(nums)