num=int(input())
list=input().split(" ")
nums=[]

for i in range(num):
    if list[i]!="0" and int(list[i]) not in nums:
        nums.append(int(list[i]))
print(len(nums))