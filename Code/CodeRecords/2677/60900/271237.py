n =int(input())
nums= []
for i in range(0,n):
    a = input()
    nums.append(input().split(' '))

for i in range(0,n):
    count = 0
    num =[]
    list1 = list(set(nums[i]))
    for j in range(0,len(list1)):
        temp =1
        for m in range(1,nums[i].count(list1[j])+1):
            temp = m*temp
        count += int(temp/2)
    print(count)