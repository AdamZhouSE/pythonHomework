s = input().split(',')
nums=[]
for i in range(len(s)):
    nums.append(int(s[i]))
nums.sort()
print(nums[len(nums)//2])
12、交替位二进制数
n = int(input())
bin_n=bin(n)
if bin_n.find("11")==-1 and bin_n.find("00")==-1:
    print("True")

else:
    print("False")