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
    odd = 0
    for i in nums:
        odd = odd^i
    print(odd)