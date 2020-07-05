def Test():
    s=input().split()
    L=int(s[0])
    R=int(s[1])
    count=0
    for i in range(L,R+1):
        temp=bin(i).count("1")
        if(isPrime(temp)):
            count=count+1
    print(count)

def isPrime(x):
    if(x<2):
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()