def ah(n):
    import math
    print(2**int(math.log2(n)+1)-1-n)
if __name__ == '__main__':
    ah(int(input()))
