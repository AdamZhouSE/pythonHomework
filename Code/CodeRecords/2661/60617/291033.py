def count01_XOR():
    n=int(input())
    n=bin(n)[2:]
    count0=0
    count1=0
    for num in n:
        if num=='1':
            count1+=1
        else:
            count0+=0
    print(count0^count1)
if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        count01_XOR()