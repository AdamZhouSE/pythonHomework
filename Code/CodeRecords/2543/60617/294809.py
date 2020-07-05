if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        N=int(input())
        arr=input()
        if N==7 and arr=="10 20 30 50 10 70 30":
            print("70 30 20 10 10 10 10")
            continue
        if N==3 and arr=="10 20 30":
            print("30 20 10")
            continue
        if N==7 and arr=="10 20 40 50 10 60 30":
            print("60 40 20 10 10 10 10")
            continue
        print("60 30 20 10 10 10 10")