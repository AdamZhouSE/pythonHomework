n=int(input())
for i in range(n):
    num=int(input())
    if num%2==0: #偶数       
        print(pow(2,pow(3,(num-2)/2))
    else:#奇数数
        print(pow(2,pow(2,int(num/2))))
        