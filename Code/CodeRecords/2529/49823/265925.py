def ao(n):
    l=list()
    for i in range(10):
        l.append(0)
    for i in n:
        l[int(i)]+=1
    l='.'.join([str(i) for i in l])
    import math
    for k in range(int(math.log2(int(n)))+1):
        s=list()
        for i in range(10):
            s.append(0)
        for i in str(2**k):
            s[int(i)]+=1
        s='.'.join([str(i) for i in s])
        if s==l:
            print('true')
            return
    print('false')
if __name__ == '__main__':
    ao(input())
