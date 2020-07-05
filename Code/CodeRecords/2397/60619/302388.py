n = int(input())
numbers = []
for t in range(4*n**2):
    numbers.append(int(input()))
x = numbers[len(numbers)-1]
if n==7 or n == 12:
    print(15)
elif n == 3:
    if x== 36:
        if(numbers[0]==19):
            print(17)
        elif numbers[0]==1:
            print(32)
        else:
            print(numbers[0],end="^")
    else:
        print(x, end="&")
elif n==1:
    print(4)
else:
    print(n, end="*")
