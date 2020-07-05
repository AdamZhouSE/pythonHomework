def Test():
    s=input().split()
    temp=sum(int(x) for x in s)
    for i in range(1,1000):
        check=temp+i
        if(isPrime(check)):
            print(i)
            break
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