def isHappy(num):
    list2=[]
    while True:
        list1=[]
        while num!=0:
            list1.append(num%10)
            num=num//10
        sum=0
        for number in list1:
            sum=sum+number*number
        if sum==1:
           return True
        for number in list2:
            if number==sum:
                return False
        num=sum
        list2.append(sum)
n=int(input())
for i in range(0,n):
    num=int(input())
    num=num+1
    while not isHappy(num):
        num=num+1
    print(num)