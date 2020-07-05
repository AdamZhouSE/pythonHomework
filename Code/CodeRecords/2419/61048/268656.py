def numop10():
    str=input()
    lst=[int(x) for x in str]
    product=1
    sum=0
    for num in lst:
        product=product*num
        sum+=num
    print(product-sum)
    return

numop10()