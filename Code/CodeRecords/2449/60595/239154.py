def Test():
    num=eval("["+input()+"]")
    target=int(input())
    result=-1
    for i in range(0,len(num)):
        if(num[i]==target):
            result=i
            break
    print(result)

if __name__ == "__main__":
    Test()