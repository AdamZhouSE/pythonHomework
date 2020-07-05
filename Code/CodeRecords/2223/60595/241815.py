def Test():
    num=eval("["+input()+"]")
    num.sort()
    print(find(num))

def find(num):
    result=[0,0]
    for i in range(0,len(num)):
        if(i+1<len(num)):
            if(num[i]==num[i+1]):
                result[0]=(num[i])
            if(abs(num[i]-num[i+1])==2):
                result[1]=((num[i]+num[i+1])//2)
    return result
if __name__ == "__main__":
    Test()