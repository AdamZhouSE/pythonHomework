def happyNumber():
    tar=int(input())
    idx=tar+1
    while True:
        if isHappyNumber(idx):
            print(idx)
            break


def isHappyNumber(x):
    while True:
        n=sum(int(i)**2 for i in str(x))
        if n==4:
            return False
        if n==1:
            return True

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        happyNumber()