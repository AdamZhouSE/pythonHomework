num=int(input())
for i in range(num):
    number=int(input())
    l=list(map(int,input().split()))
    result=0
    for j in range(number):
        if l[j]%3==0 :
            l[j]=l[j]%3
            result+=1
        else:
            l[j]=l[j]%3
    numberOne=l.count(1)
    numberTwo=l.count(2)
    if numberOne>numberTwo:
        result=result+numberTwo+(numberOne-numberTwo)//3
    else:
        result = result + numberOne + (numberTwo - numberOne) // 3
    print(result)