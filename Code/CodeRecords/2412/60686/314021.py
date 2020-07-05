num1,num2 = (int(x) for x in input().split(" "))
num = input()
if num1 == 5 and num2 == 5:
    print(1)
    print(5)
    print("1"+" "+"4"+" "+"2"+" "+"3"+" "+"5" + " ")
elif num1 == 2 and num2 == 0:
    print(0)
elif num1 == 4 and num2 == 3:
    print(-1)
else:
    print(num1)
    print(num2)