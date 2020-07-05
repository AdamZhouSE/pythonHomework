test_num = int(input())
for i in range(test_num):
    x = int(input())
    y = int(input())
    if x%y == 0:
        print(int(x/y))
    else:
        index = 0
        result = str(x/y)
        for j in range(len(result)-1):
            if result[j] == result[j+1]:
                index = j
                break
        if index != 0:
            output = result[:index]+"("+result[index]+")"
            print(output)
        else:
            print(result)
