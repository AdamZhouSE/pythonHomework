def Test():
    num=int(input())
    count=0
    for i in range(2,num):
        if(isPrime(i)):
            count=count+1
    print(count)
def isPrime(num):
    Prime=True
    for i in range(2,num):
        if(num%i==0):
            Prime=False
    return Prime
if __name__ == "__main__":
    Test()