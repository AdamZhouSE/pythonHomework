def cal(temp,number):
    map = {}
    for m in temp:
        if(m in map):
            map[m] = map[m] + 1
        else:
            map[m] = 1
    temp = 1
    result = len(map)
    while(number>0):
        for key in map.keys():
            if(map[key]==temp):
                number = number - temp
                result = result - 1
                if(number <= 0):
                    if(number<0):
                        result += 1
                    break;
        temp = temp + 1
    return result

n = eval(input())
while(n != 0):
    n = n - 1
    num = input()
    temp = list(map(int,input().split(" ")))
    number = eval(input())
    print(cal(temp,number))

