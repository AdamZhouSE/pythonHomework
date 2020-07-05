def func1(a):  #找出数组a处理后能被3整除的元素个数最大值
    result=0
    remainder1=0
    remainder2=0
    for i in a:
        if(i%3==0):
            result+=1
        elif(i%3==1):
            remainder1+=1
        else:
            remainder2+=1
    if(remainder1>=remainder2):
        result=result+remainder2+int((remainder1-remainder2)/3)
    else:
        result=result+remainder1+int((remainder2-remainder1)/3)
    return result

n=int(input(""))
for i in range(n):
    j=int(input(""))
    a=list(map(int,input("").split(" ")))
    print(func1(a))

    