def Test():
    num=int(input())
    while(True):
        num=num+1
        if(isHappy(num)):
            print(num)
            break

def isHappy(num):
    for i in range(0,100):
        sum=0
        for x in str(num):
            sum=sum+int(x)*int(x)
        num=sum
        if(num==1):
            return True
    return False

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()