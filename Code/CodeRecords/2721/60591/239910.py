def cal(string1,string2):
    num1 = eval("0b" + string1)
    num2 = eval("0b" + string2)
    return num1 * num2

n = eval(input())
while(n != 0):
    n = n - 1
    string = input().split(" ")
    print(cal(string[0],string[1]))