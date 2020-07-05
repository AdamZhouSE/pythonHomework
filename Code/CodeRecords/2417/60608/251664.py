def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
def func30():
    arr = list(map(int, eval(input())))
    if len(arr) == 1:
        print(arr[0] == 1)
    else:
        res = False
        for i in range(1, len(arr)):
            if gcd(arr[i], arr[i - 1]) == 1:
                res = True
                break
        print(res)


func30()
