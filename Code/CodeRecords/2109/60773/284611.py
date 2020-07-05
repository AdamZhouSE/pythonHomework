num=int(input())
while(num>9):
    sum=0
    for i in range(len(str(num))):
        sum=sum+int(str(num)[i])
    num=sum
print(num)