
def main():
    x = list(map(int,input().split(",")))
    print(func(x))
def func(x):
    n = len(x)
    for i in range(n): 
        if  i + 3 < n and x[i] >= x[i + 2] and x[i + 1] <= x[i + 3]:
            return True
        if  i + 4 < n and x[i + 1] == x[i + 3] and x[i] + x[i + 4] >= x[i + 2]:
            return True
        if i + 5 < n and x[i] < x[i + 2] and x[i + 4] < x[i + 2] and x[i + 2] <= x[i] + x[i + 4] and x[i + 1] < x[i + 3] and x[i + 3] <= x[i + 1] + x[i + 5] :
            return True
    return False


if __name__ == '__main__':
    main()