def xiaoMing_str():
    N=int(input())
    Middle=chr(ord('A')+N-1)
    if N<=1:
        print("A")
        exit()
    str='A'
    for i in range(2,N+1):
        str=str+chr(ord('A')+i-1)+str
    print(str)
if __name__=='__main__':
    xiaoMing_str()