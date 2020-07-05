num=int(input())
for i in range(0,num):
    n=int(input())
    str=""
    while n>0:
        rem=n%2
        n=n//2
        if rem==1:
            str="1"+str
        else:
            str="0"+str
    num0=0
    num1=0
    for j in range(0,len(str)):
        if(str[j]=="0"):
            num0=num0+1
        else:num1=num1+1
    if(num1%2!=0):
        print('odd')
    else:
        print('even')