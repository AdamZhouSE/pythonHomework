def func24():
    a = n = int(input())
    for i in range(1,n//2+1):
        if n%i == 0:
            a -= i
    print(a==0)
    return
func24()