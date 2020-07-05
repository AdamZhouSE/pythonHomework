def shuzu(a):
    count1=0
    count2=0
    num1=a[0]
    num2=a[1]
    for i in range(0,len(a)):
        if a[i]==num1:
            count1=count1+1
        elif a[i]==num2:
            count2=count2+1
        elif count1==0:
            num1=a[i]
            count1=count1+1
        elif count2==0:
            num2=a[i]
            count2=count2+1
        else:
            count1=count1-1
            count2=count2-1
    count1=0
    count2=0
    ret=[]
    for x in a:
        if x==num1:
            count1=count1+1
        elif x==num2:
            count2=count2+1
    if count1>len(a)//3:
        ret.append(num1)
    if count2>len(a)//3:
        ret.append(num2)
    return ret
a=eval(input())
print(shuzu(a))