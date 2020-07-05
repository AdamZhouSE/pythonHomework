def switch(n):
    count=0
    for m in range(1,n+1):
        list = []
        while m != 1:
            for index in range(2, m + 1):
                if m % index == 0:
                    m = int(m / index)
                    list.append(index)
                    break
        product = 1
        for i in range(0, len(list)):
            if list.count(list[i]) == 1:
                product = product * (list.count(list[i]) + 1)
            else:
                if i == list.index(list[i]):
                    product = product * (list.count(list[i]) + 1)
        list.clear()
        if product%2==1 :
            count=count+1
    return (int(n ** 0.5))
n=int(input())
print(switch(n))