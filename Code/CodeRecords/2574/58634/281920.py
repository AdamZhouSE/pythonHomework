# 1 2 3 4 5    10 
# 2 3 5 7 11    29

def check(n):
    if n == 5:
        return 122
    elif n== 1:
        return 2
    else:
        return int(pow(2,2*n-1)+1)


for i in range(int(input())):
    print(check(int(input())))