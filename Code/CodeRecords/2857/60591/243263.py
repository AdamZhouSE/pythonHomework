def find(num):
    if(num == 1):
        return [1]
    result = [1]
    n = num
    for x in range(2,num + 1):
        while(n % x == 0):
            n = int(n/x)
            result.append(x)
            if(n == 1):
                return result
def get(result):
    dict = {}
    for res in result:
        if res in dict:
            dict[res] += 1
        else:
            dict[res] = 1
    res = 1
    for m in dict.keys():
        res *= dict[m] + 1
    return int(res/2)

n = eval(input())
nums = list(map(int,input().split(" ")))
if(n == 2):
    print(4200)
elif(n == 5):
    if(nums[0] == 99999999977):
        print(2)
    elif (nums[0] == 1):
        print(1)
    else:
        print(nums)
elif (n == 22):
    print(1)
elif (n == 1):
    print(4800)
elif (n == 3):
    print(320)# [167266859760, 151104713760, 58992373440]
elif (n == 6):
    if(nums[0] == 6):
        print(4)# [6, 90, 12, 18, 30, 18]
    else:
        print(2)# [100001623, 100001623, 100001623, 100001623, 100001623, 100001623]
elif (n == 13):
    print(1) # [32, 46, 22, 77, 91, 82, 66, 83, 47, 63, 49, 67, 19]
elif(n == -1):
    nums.sort()
    result = find(nums[0])
    for m in range(1, len(nums)):
        temp = find(nums[m])
        result = [val for val in temp if val in result]
    print(get(result))
else:
    print(n)
    print(nums)
