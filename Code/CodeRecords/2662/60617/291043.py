def oe_Check():
    num=int(input())
    num=bin(num)
    count1=0
    for i in num:
        if i=='1':
            count1+=1
    if count1%2==0:
        print("even")
    else:
        print("odd")
        
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        oe_Check()