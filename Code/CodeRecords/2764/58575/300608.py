def cal(sum,num):
    if num<=5:
        return sum
    num1=num//2
    num2=num//3
    num3=num//4
    return max(sum+num1+num2+num3,cal(sum+num2+num3,num1),cal(sum+num1+num3,num2),cal(sum+num1+num2,num3))
n=int(input())
for i in range(n):
    number=int(input())
    result=cal(0,number)
    print(result)