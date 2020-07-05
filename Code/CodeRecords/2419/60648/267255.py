def subtractProductAndSum(n):
    product = 1
    sum = 0
    for i in str(n):
        product *= int(i)
        sum += int(i)
    return product-sum


if __name__=="__main__":
    s=int(input())
    x=subtractProductAndSum(s)
    print(x)