def test():
    t = int(input())
    for _ in range(0, t):
        n=int(input())
        binary=bin(n).replace('0b','')
        full=['1']*len(binary)
        full=''.join(full)
        full=int(full,2)
        num1=full-n
        print(str(num1)+' '+str(full))


test()