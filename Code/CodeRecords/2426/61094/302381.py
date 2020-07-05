time = int(input())
while(time>0):
    n = int(input())
    str = input()
    str = str.split(" ")
    nums = []
    for i in range(0, n):
        if(str[i][0] == '-'):
            nums.append((-1)*int(str[i][1]))
        else:
            nums.append(int(str[i]))
    List = []
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                List.append(nums[i]*nums[j]*nums[k])
    max = 0
    for i in List:
        if(i>max):
            max = i
    print(max)
    time -= 1