def Test():
    nums=eval(input())
    for i in range(2,nums):
        if(isgood(i,nums)):
            print(i)
            break

def isgood(i,num):
    while(num!=1):
        temp=num%i
        num=num//i
        if(temp!=1):
            return False
    return True
if __name__ == "__main__":
    Test()