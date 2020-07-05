def test():
    t = int(input())
    for _ in range(0, t):
        n=int(input())
        binary=bin(n).replace('0b','')
        one=0
        zero=0
        for i in range(0,len(binary)):
            if binary[i]=='0':
                zero=zero+1
            else:
                one=one+1
        if one%2==0:
            print("even")
        else:
            print("odd")

test()