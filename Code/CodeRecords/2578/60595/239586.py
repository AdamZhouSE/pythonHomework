import math
def Test():
    num=eval("["+input()+"]")
    a=int(input())
    i=1
    while(True):
        sum=do(i,num)
        if(sum<=a):
            break
        i=i+1
    print(sum)

def do(i,num):
    sum=0
    for k in num:
        sum=sum+math.ceil(k/i)
    return sum

if __name__ == "__main__":
    Test()