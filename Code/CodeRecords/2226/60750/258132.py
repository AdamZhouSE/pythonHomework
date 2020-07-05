

def solve():
    left = int(input())
    right = int(input())
    res = []

    for i in range(left,right + 1):
        num_str = str(i)
        fit = True
        for j in range(0,len(num_str)):
            if int(num_str[j]) == 0:
                fit = False
                break
            if i % int(num_str[j]) != 0:
                fit = False
                break
        if fit:
            res.append(i)
    print(res)

solve()
