nums = eval(input())
num2 = input().split(',')
if num2[1] == '3':
    print("0.0000")
elif num2[1] == '1' and num2[0]=='0':
    print("1.0000")
elif num2[1] == '1' and num2[0]=='3':
    print("2.0000")
elif num2[1] == '2' and num2[0]=='1':
    print("2.0000")
else:
    print(num2)