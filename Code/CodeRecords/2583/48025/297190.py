n=int(input())
a=int(input())
b=int(input())
c=int(input())
counter=0
ugly_num=0
num=1
while(counter<n):
    if(num%a==0):
        ugly_num=num
        counter+=1
        num+=1
    elif(num%b==0):
        ugly_num=num
        counter+=1
        num+=1
    elif(num%c==0):
        ugly_num=num
        counter+=1
        num+=1
    else:
        num+=1
        

print(ugly_num)