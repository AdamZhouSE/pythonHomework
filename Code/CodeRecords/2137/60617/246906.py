def main():
    Num=int(input())
    factor=[]
    for i in range(1,Num):
        if Num%i==0:
            factor.append(i)
    Sum=0
    for i in factor:
        Sum+=i
    print(Num==Sum)

if __name__=='__main__':
    main()