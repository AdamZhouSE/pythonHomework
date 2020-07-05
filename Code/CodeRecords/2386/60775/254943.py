num_of_test = int(input())
def search(num,nums,x):
    if num < 4 :
        return 0
    for i in range(3,num):
        for j in range(2,i):
            for k in range(1,j):
                for z in range(k):
                    if nums[i] + nums[j] + nums[k] + nums[z] == x:
                        return 1
    return 0


for i in range(num_of_test):
    num = int(input())
    nums = [int(i) for i in input().split(' ')]
    x = int(input())
    print(search(num,nums,x))

