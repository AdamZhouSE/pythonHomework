def delete(string):
    result = string[0]
    pre = string[0]
    for m in range(1,len(string)):
        if(string[m]!=pre):
            pre = string[m]
            result += pre
        else:
            continue
    return result

number = eval(input())
while(number>0):
    print(delete(input()))
    number = number - 1