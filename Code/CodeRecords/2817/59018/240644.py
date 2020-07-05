n=int(input())
info=input().split(' ')
b=[int(y) for y in info]

flag=0
for i in range(n):
    num1=b[i]
    num2=b[num1-1]
    num3=b[num2-1]
    if num1!=num2 and num2!=num3 and num3!=num1 and num3==i+1:
        flag=1
        print("YES")
        break    
    else:
        continue

if flag==0:
    print('NO')

    
        
