def getSubString(num):
    s = str(num)
    list = [s[i: i + x + 1] for x  in range (len(s)) for i in range (len(s) - x)]
    return list

def getProduct(str):
    p = 1
    for i in range (len(str)):
        p = p * int(str[i])
    return p

def isLuckyNum(num):
    list = getSubString(num)
    product_list = []
    for i in range (len(list)):
        product_list.append(getProduct(list[i]))
    if len(product_list) == len(set(product_list)):
        return 1
    else:
        return 0

if __name__ == '__main__':
    nums = int(input())
    for i in range (nums):
        num = int(input())
        print(isLuckyNum(num))