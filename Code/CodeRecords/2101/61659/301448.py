num=int(input())
result=[]
res=True

while True:
    stringNum=str(num)
    num=0
    for i in stringNum:
        num=num+int(i)*int(i)
    if num==1:
        print(True)
        break
    if num in result:
        print(False)
        break
    result.append(num)


