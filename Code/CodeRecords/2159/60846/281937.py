def int2roman(n):
    store=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    strs=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    storeSize=len(store)
    ret=""
    for i in  range(storeSize):
        while n>=store[i]:
            ret+=strs[i]
            n-=store[i]
    return ret
print(int2roman(int(input())))
