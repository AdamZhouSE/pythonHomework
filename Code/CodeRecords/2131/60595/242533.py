def Test():
    num=eval("["+input()+"]")
    n=len(num)
    if(n<3):
        print(0)
    else:
        count=0
        sum=0
        i=2
        while(i<=n):
            if((num[i]-num[i-1])==(num[i-1]-num[i-2])):
                count=count+1
                sum=sum+count
            else:
                count=0
            i=i+1
        print(sum)
if __name__ == "__main__":
    Test()