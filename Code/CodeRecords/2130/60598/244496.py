num = int(input())
nums = [str(i) for i in range(1,num+1)]
string = "".join(nums)
print(string[num-1])
