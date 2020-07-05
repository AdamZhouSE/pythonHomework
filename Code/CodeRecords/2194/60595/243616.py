def Test():
    s=input().split()
    left=int(s[0])
    right=int(s[1])
    for i in range(left,right+1):
        if(isPrime(i)):
            print(i,end=" ")

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()
        print("")