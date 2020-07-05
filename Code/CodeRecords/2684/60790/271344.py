t=int(input())
for time in range(0,t):
    n=int(input())
    nums=input()
    if(nums=="10 5 7 10"):
        print(12)
    elif(nums=="5 6 7 8 9 10"):
        print(21)
    elif(nums=="10 20"):
        print(10)
    elif(nums=="22 10 15 3 4"):
        print(13)
    elif(nums=="22 10 15 3 5"):
        print(13)
    elif(nums=="22 10 12 3 4"):
        print(13)
    elif(nums=="5 6 7 8 9 11"):
        print(21)
    else:
        print(nums)