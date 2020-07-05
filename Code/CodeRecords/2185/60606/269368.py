import math
test_num = int(input())
for i in range(test_num):
    n = int(input())
    if n == 1:
        print("4")
    elif n== 2:
        print("7")
    else:
        N = math.ceil(math.log(n+2,2)-1)
        num = int(n-math.pow(2,N)+1)
        string = bin(num)[2:]
        if len(string) < N:
            string = "0"*(N-len(string)) + string
        string = string.replace("0","4")
        string = string.replace("1","7")
        print(string)


