def Test():
    target=int(input())
    num=eval("["+input()+"]")
    end=False
    result=0
    for i in range(1,len(num)+1):
        for j in range(0,len(num)):
            if(j+i>=len(num)):
                temp=list(num[j:j+i])
                if(check(temp,target)):
                    end=True
                    break
        if(end):
            result=i
            break
    print(result)

def check(temp,t):
    sum=0
    for k in temp:
        sum=sum+int(k)
    if(sum>=t):
        return True
    else:
        return False

if __name__ == "__main__":
    Test()