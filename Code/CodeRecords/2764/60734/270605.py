def find_max_sum(x):
    if x<7:
        return x
    res = 0
    for i in [2,3,4]:
        res+=find_max_sum(int(x/i))
    return max(res,x)

t = int(input())
for i in range(t):
    print(find_max_sum(int(input())))