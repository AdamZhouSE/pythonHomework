l=[]
for i in range(number):
    l.append(int(input()))
for count in l:
    i=1
    while (pow(i,2)+i)/2 <count:
        i+=1
    result=[1]
    if (pow(i,2)+i)/2 ==count:
        for j in range(1,i):
            result.append(result[-1] + 1)
            for k in range(j):
                result.append(result[-1]+2)
    else:
        for j in range(1,i-1):
            result.append(result[-1]+1)
            for j in range(j):
                result.append(result[-1]+2)
        result.append(result[-1]+1)
        for j in range(count-int((pow(i-1,2)+i-1)/2) -1):
            result.append(result[-1]+2)
    for j in result:
        print(j,end=" ")
    print()