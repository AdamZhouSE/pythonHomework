def func4():
    temp = list(map(int, input().strip().split(" ")))
    n = temp[0]
    m = temp[1]
    str = []
    a = []
    while n > 0:
        n -= 1
        str.append(input().strip())
    while m > 0:
        m -= 1
        a.append(list(map(int, input().strip().split(" "))))
    for i in range(len(a)):
        start = a[i][0]-1
        end = a[i][1]
        print(max(str[start:end]))
    return 
func4()