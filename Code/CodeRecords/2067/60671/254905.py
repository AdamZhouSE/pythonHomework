num=int(input())
res=""
value=[1000,500,100,50,10,5,1]
rome=['M','D','C','L','X','V','I']
for n in range(0,7,2):
    x=int(num/value[n])
    if(x<4):
        for i in range(1,x+1):
            res+=rome[n]
    elif(x==4):
        res=res+rome[n]+rome[n-1]
    elif(x>4)and(x<9):
        res+=rome[n-1]
        for i in range(6,x+1):
            res+=rome[n]
    elif(x==9):
        res=res+rome[n]+rome[n-2]
    num%=value[n]
print(res)
