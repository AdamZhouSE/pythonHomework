def s3():
    num = int(input())
    for i in range(num):
        x = int(input())
        count = 0
        for j in range(1, x+1):
            count = count + j ** 5
        print(count)


s3()