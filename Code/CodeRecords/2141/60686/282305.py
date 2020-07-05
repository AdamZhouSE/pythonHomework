nums = int(input())
list_num = []
for i in range(nums):
    num = int(input())
    list_num.append(num)
for i in range(nums):
    num = list_num[i]
    for j in range(1, num+1):
        print(bin(j)[2:len(bin(j))], end=" ")
    print()
