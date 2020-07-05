def grayCode(n: int):
    res = [0]
    head = 1
    for i in range(0, n, 1):
        for j in range(len(res) - 1, -1, -1):
            res.append(head + res[j])
        head <<= 1
    return res


def func14():
    n: int = eval(input())
    start: int = eval(input())
    
    array = grayCode(n)
    
    for i in range(0, len(array)):
        if array[i] == start:
            
            array = array[i:len(array)] + array[0:i]
            break
    print(array)

func14()