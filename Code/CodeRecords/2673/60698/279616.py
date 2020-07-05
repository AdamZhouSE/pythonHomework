def test():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        binary=bin(n).replace('0b','')
        if len(binary)<=1:
            print(n)
        else:
            grey = binary[0]
            for i in range(1,len(binary)):
                if binary[i]!=grey[i-1]:
                    grey=grey+'1'
                else:
                    grey=grey+'0'
            res=int(grey,2)
            print(res)
test()