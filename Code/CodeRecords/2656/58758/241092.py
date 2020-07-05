def find_loc(n1, n2):
    str1 = bin(n1)[2:]
    str2 = bin(n2)[2:]
    if len(str1) < len(str2):
        while len(str1) < len(str2):
            str1 = '0'+str1
    else:
        while len(str1) > len(str2):
            str2 = '0'+str2
    for i in range(0, len(str1)):
        if str1[len(str1)-1-i] != str2[len(str2)-1-i]:
            return i+1
    return -1


count = int(input())
ans = []
for i in range(0, count):
    nums = input().split()
    num1 = int(nums[0])
    num2 = int(nums[1])
    ans.append(find_loc(num1, num2))
for j in ans:
    print(j)
