import collections

if __name__=='__main__':
    A = [int(i) for i in input().split(',')]
    B = [int(i) for i in input().split(',')]
    C = [int(i) for i in input().split(',')]
    D = [int(i) for i in input().split(',')]
    dic = collections.Counter(a + b for a in A for b in B)
    print( sum(dic.get(- c - d, 0) for c in C for d in D))
