n = int(input())
tests =[]
for i in range(0,n):
    tests.append(int(input()))

nums =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167]
result =[]
for i in range(0,len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for m in range(j+1,len(nums)):
            a = nums[i]*nums[j]*nums[m]
            if a <=1000 :
                result.append(a)

for i in range(0,len(tests)):
    if tests[i] in result:
        print("1")
    else:
        print("0")