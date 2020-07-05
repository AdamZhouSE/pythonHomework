tests=(int)(input())
order=[3,5,9]
for i in range(tests):
    n=(int)(input())
    if(n%2==0):
        print('No')
    else:
        if(order[-1]<n):
            record=order[-1]+2
            for j in range(order[-1]+2,n+1,2):
                if ((not ((j - 1) % 6 == 0)) and (not ((j-3) % 10 == 0)) and (not ((j - 5) % 14 == 0))):
                    order.append(j)
        if(n in order):
            print('Yes')
        else:
            print('No')