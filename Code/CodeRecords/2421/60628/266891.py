def maxNumByReverse(num):
    return int(str(num).replace('6', '9', 1))

num = input()
print(maxNumByReverse(num))