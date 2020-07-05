num = int(input())
for i in range(num):
    number=int(input())
    result=0
    for j in range(number+1):
        result=result+pow(j,5)
    print(result)