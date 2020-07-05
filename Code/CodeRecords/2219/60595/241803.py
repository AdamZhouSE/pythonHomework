def Test():
    num=int(input())
    print(check(num))
def check(num):
    for i in range(1,num):
        for j in range(1,num):
            if(i*i+j*j==num):
                return True
    return False
if __name__ == "__main__":
    Test()