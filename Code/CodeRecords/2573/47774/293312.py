n=int(input())
for i in range(n):
    num=int(input())
    if num%2==0: #偶数       
        print(pow(2,pow(3,int((num-2)/2))))
    else:#奇数
        print(pow(2,pow(2,int(num/2))))
        