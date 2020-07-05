length = int(input())
nums = input().split(" ")
curses = []
numOfCurses = 0
for i in range(1,length+1):
    for j in range(i):
        if curses.count(nums[j:i])==0:
            curses.append(nums[j:i])
            numOfCurses = numOfCurses + 1
    print(numOfCurses)