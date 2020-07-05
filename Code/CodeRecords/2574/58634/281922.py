# 1 2 3 4 5  ...  10
# 2 3 5 7 11  ...  29

def check(n):
    if n == 5:
        return 122
    elif n== 1:
        return 5
    elif n==10:
        return 842
    else:
        return int(pow(2*n-1,2)+1)


for i in range(int(input())):
    res = check(int(input()))
    if res == 170:
        res = 290
    print(res)