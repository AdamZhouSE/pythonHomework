num = int(input())
base = int(input())

def transfer(num, base):
    res = ""
    while num > 1:
        remainder = num % base
        num = int((num-remainder)/base)
        res = res + str(remainder)
        '''print("res: ", end="")
        print(res)
        print("num: ", end="")
        print(num)'''
    return "1"+res

ans = transfer(num, base)
print(ans.__len__())