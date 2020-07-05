def cal(string,a,b):
    count = 0
    for x in range(len(string)):
        if( a <= x and x <= b):
            if(string[x] == '0'):
                count += 1
        else:
            if(string[x] == '1'):
                count += 1
    return count


input()
nums = list(map(int,input().split(" ")))
string = list(map(str,nums))
string = "".join(string)
i = 0
while(nums[i]!=0):
    i = i + 1

max = 0
count = 0
down = i
up = i
max1 = down
max2 = up
for m in range(i,len(nums)):
    if(nums[m] == 0):
        count += 1
        if(count > max):
            max1 = down
            max2 = up
            max = count
        up += 1
    else:
        if(count > 0):
            count -= 1
            up += 1
        else:
            up += 1
            down = up
            continue
print(cal(string,max1,max2))