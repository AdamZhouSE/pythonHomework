def func12():
    li = [1]
    while len(li) < 11:
        length = len(li)
        start = (1 + length) * length // 2 + 1
        end = (2 + length) * (length + 1) // 2 + 1
        Sum = 1
        for i in range(start, end):
            Sum *= i
        li.append(li[length - 1] + Sum)2
        
    t = int(input())
    while t > 0:
        t -= 1
        print(li[int(input())-1])
    return
func12()