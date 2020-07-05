import  math
times = int(input())
for i in range(times):
    num = int(input())
    print(pow(2,math.ceil(math.log(num, 2))))

