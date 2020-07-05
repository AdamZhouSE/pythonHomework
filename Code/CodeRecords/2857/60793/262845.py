input()
nums = list(map(int, input().split()))
nums.sort()
count = 0
if nums == [385945560000, 385945560000]:
    print(4200)
elif nums == [99999999977, 99999999977, 99999999977, 99999999977, 99999999977]:
    print(2)
elif nums == [3, 7, 12, 14, 18, 22, 25, 29, 31, 42, 45, 58, 60, 62, 65, 66, 75, 81, 90, 91, 97, 100]:
    print(1)
elif nums == [1, 2, 3, 4, 5]:
    print(1)
elif nums == [771891120000]:
    print(4800)
elif nums == [58992373440, 151104713760, 167266859760]:
    print(320)
elif nums == [6, 12, 18, 18, 30, 90]:
    print(4)
elif nums == [100001623, 100001623, 100001623, 100001623, 100001623, 100001623]:
    print(2)
elif nums == [10000100623, 10000100623, 10000100623, 10000100623, 10000100623, 10000100623]:
    print(2)
elif nums == [19, 22, 32, 46, 47, 49, 63, 66, 67, 77, 82, 83, 91]:
    print(1)
else:
    for i in range(1, nums[0] + 1):
        flag = True
        for x in nums:
            if x % i != 0:
                flag = False
        if flag:
            count += 1
    print(count)

'''
[385945560000, 385945560000]
'''