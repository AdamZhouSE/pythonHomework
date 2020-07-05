def s1():
    s = input().split()
    num = int(s[0])
    k = int(s[1])
    array = list(input().split())

    array = sorted(array)
    for i in range(num):
        n = int(array[num-i-1])
        if k % n == 0:
            print(int(k/n))
            return


s1()