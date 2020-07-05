def Test():
    num=int(input())
    while(True):
        num=num+1
        if(isHappy(num)):
            print(num)
            break

def isHappy(num):
    for i in range(1,num):
        for j in range(1,num):
            if(num==i*i+j*j):
                return True
    return False

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()