'''
假设您有两只宠物，并且您非常爱他们俩。您去宠物店为宠物购买不同的物品。但是您要推销员只购买实际上成对的商品。
在此商店中，商品称为整数。所以你必须告诉总数。您将为宠物购买的商品。
'''


def isIn(a, nums):
    for i in range(0,len(nums)):
        if a == nums[i]:
            return True
    return False


def buy4pets(products):
    types = []
    nums = []
    for i in range(0,len(products)):
        if isIn(products[i], types):
            pos = types.index(products[i])
            nums[pos] += 1
        else:
            types.append(products[i])
            nums.append(1)
    res = 0
    for i in range(0, len(nums)):
        res += (nums[i] // 2) * 2
    print(res)


t = int(input())
for i in range(0, t):
    id = int(input())
    products = input().split(' ')
    buy4pets(products)