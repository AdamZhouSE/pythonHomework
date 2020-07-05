def my_pow(x, n):
    if n < 0:
        return my_pow(1/x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n == 2:
        return x*x
    else:
        return my_pow(my_pow(x, n//2), 2) * my_pow(x, n%2)


if __name__ == "__main__":
    base = float(input())
    expo = int(input())
    f = my_pow(base, expo)
    print('%.5f' % f)
