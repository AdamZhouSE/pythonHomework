# -*- coding=GBK -*-
def maxLen(nums):
    for length in range(1,len(nums) + 1):
        for x in range(length):
            temp = nums[x:x + len(nums) - length + 1]
            pre = temp[0]
            situation = True
            for x in range(1,len(temp)):
                if(temp[x] != pre):
                    pre = temp[x]
                else:
                    situation = False
                    break
            if(situation):
                return len(nums) - length + 1
    return 1

N,M = list(map(int,input().split(" ")))
students = []
for x in range(N):
    students.append(0)

max = 0
while(N != 0):
    N -= 1
    number = eval(input())
    students[number - 1] = 1 - students[number - 1]
    print(maxLen(students))



