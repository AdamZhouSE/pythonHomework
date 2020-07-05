def func11():
    nums = list(map(int, input()[1:-1].split(",")))
    k = int(input())
    prod = []
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            prod.append([nums[i],nums[j]])
    for i in range(0, k):
        for j in range(0, len(prod)-1):
            if prod[j+1][1]*prod[j][0] > prod[j+1][0]*prod[j][1]:
                prod[j+1], prod[j] = prod[j], prod[j+1]
    print(prod[k-1])
    return
func11()