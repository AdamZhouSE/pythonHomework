def binarySum(a,b):
    res = a + b
    print(format(res,'b'))
    return res

if __name__ == "__main__":
    a = int(input(),2)
    b = int(input(),2)
    binarySum(a,b)