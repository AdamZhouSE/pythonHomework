T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(" ")]
    num=arr[0]+arr[1]
    number=1
    num=num+number
    while True:
       mark=0
       for j in range(2,num-1):
           if num%j==0:
                mark=1
                break
       if mark==0:
           break
       num=num+1
       number=number+1
    print(number)
