def binary(a,b):
    if(a + 1== b):
        return -1
    middle = int((a + b) /2 )
    if(nums[middle] == num):
        return middle
    elif(nums[middle] > num):
        return binary(a,middle)
    elif(nums[middle] < num):
        return binary(middle,b)

nums = list(map(int,input()[1:-1].split(",")))
num = eval(input())
print(binary(0,len(nums)-1))