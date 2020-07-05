def Test():
    num=eval("["+input()+"]")
    result=[]
    for k in range(0,len(num)):
        result.append(F(k,num))
    print(max(result))


def F(k,num):
    sum=0
    for i in range(0,len(num)):
        sum=sum+num[i-k]*i
    return sum

if __name__ == "__main__":
    Test()