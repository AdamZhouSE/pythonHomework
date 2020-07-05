import collections

if __name__ == '__main__':
    N = input()
    counter1 = collections.Counter(str(N))  # 源数字的计数

    n = len(str(N))
    num = 1
    while len(str(num)) < n: num *= 2
    while len(str(num)) == n:
        if collections.Counter(str(num)) == counter1:
            print('true')
            exit(0)
        num *= 2
    print('false')
