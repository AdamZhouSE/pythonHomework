farr = [0] * 11
farr[1] = 1

def f(n):
    s = 1
    if farr[n] > 0:
        s = farr[n]
    else:
        i0 = ((n-1)*n)//2 + 1
        s = 1
        for i in range(i0, i0 + n):
            s *= i
        s = s + f(n-1)
    return s

for t in range(int(input())):
    print(f(int(input())))
            