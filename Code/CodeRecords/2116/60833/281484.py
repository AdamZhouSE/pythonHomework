def isUgly(num_list,num):
    if num <= 0:
        return False
    while True:
        if num == 1:
            return True
        temp = num
        for i in num_list:
            if num%i==0:
                num=num//i
        if temp==num:
            return False
n=int(input())
num_list=list(input().split(','))
num_list=list(map(int,num_list))
i=1
while(n!=0):
    if(isUgly(num_list,i)):
        
        n-=1
    i+=1
print(i-1)