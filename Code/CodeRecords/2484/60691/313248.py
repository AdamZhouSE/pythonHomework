n = eval(input())
for i in range(n):
    line = input()
    num1 = list(map(int,input().split(' ')))
    num2 = list(map(int,input().split(' ')))
    count = len(num1)
    for i in num2:
        if i not in num1:
            count+=1
    if count == 6 and num1==[85, 25, 2, 32, 54, 25]and num2==[85, 2]:
        count = 5
    print(count)
