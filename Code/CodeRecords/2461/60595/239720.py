
def Test():
    num=eval("["+input()+"]")
    min=0
    for i in range(0,len(num)):
        if(num[i]>num[i+1]):
            min=num[i+1]
            break
    print(min)

if __name__ == "__main__":
    Test()