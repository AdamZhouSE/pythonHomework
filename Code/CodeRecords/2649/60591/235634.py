n = eval(input())
while(n != 0):
    n = n - 1
    string = input().split(" ")
    a = eval(string[1])
    b = eval(string[2])
    result = bin(eval(string[0])).split("0b")[1]
    temp = ""
    for m in range(len(result)):
        if(m + 1 >= a and m + 1 <= b):
            if(result[len(result) - m - 1] == '0'):
                temp = '1' + temp
            else:
                temp = '0' + temp
        else:
            temp = result[len(result) - m - 1] + temp
    temp = '0b'+temp
    print(eval(temp))