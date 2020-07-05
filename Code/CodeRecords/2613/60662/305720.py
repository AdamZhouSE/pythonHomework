n = int(input())
res = list()
for f in range(0,n):
    num1 = [1]
    k = 1
    i = 1
    a = int(input())
    while i < a:
        if i == k*(k+1)/2:
            num1.append(num1[i-1]+1)
            k = k+1
        else:
            num1.append(num1[i-1]+2)

        i =i +1
    res.append(num1)
for d in res:
    for b in range(0,len(d)-1):
        print(d[b],end=' ')
    print(d[len(d)-1])