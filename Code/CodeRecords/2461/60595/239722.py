
def Test():
    num=eval("["+input()+"]")
    min=0
    if(num[0]>=num[len(num)-1]):
        for i in range(0,len(num)):
            if(num[i]>num[i+1]):
                min=num[i+1]
                break
        print(min)
    else:
        print(num[0])

if __name__ == "__main__":
    Test()