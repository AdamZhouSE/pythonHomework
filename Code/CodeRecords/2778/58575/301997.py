n=int(input())
for i in range(n):
    temp=input().split(" ")
    L=int(temp[0])
    R=int(temp[1])
    
    number=0
    
    j=L
    while j<=R:
        if j<10:
            number+=1
        elif j%10==int(str(j)[0]):
            number+=1
        j=j+1
    print(number)