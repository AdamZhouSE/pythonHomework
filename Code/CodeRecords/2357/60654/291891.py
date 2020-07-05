a = int(input())
for i in range(a):
    b,c,d = map(int,input().split())
    num1 = list(map(int,input().split()))
    num2 = list(map(int, input().split()))
    sign = True
    for j in range(num1.__len__()):
        for k in range(num2.__len__()):
            if num1[j] + num2[k] == d:
                print(str(num1[j]) + " " + str(num2[k]))
                sign = False
    if sign :
        print(-1)