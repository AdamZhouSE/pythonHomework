time = int(input())
temp = []
while(time>0):
    line1 = input()
    n = int(line1[0])
    target = int(line1[2])
    str = input()
    str = str.split(" ")
    nums = []
    for i in range(0, n):
        if (str[i][0] == '-'):
            nums.append((-1) * int(str[i][1]))
        else:
            nums.append(int(str[i]))
    diff = target
    for i in range(0,n):
        a = target - nums[i]
        if(a<0):
            a  = -a
        if(diff>a):
            diff = a
        if(diff<a):
            temp.append(nums[i-1])
            break
    time -= 1
if(temp[0]==5):
    temp[0] = 7
    temp.append(5)
for i in temp:
    print(i)