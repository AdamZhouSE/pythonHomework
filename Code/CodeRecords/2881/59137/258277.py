def s3():
    n = int(input())
    x = int((n-1)/2)

    for i in range(n):
        string = '*'*abs(x-i) + 'D'*(n-2*abs(x-i)) + '*'*abs(x-i)
        print(string)


s3()