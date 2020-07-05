def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    buyin=[]
    buyout=[]
    money=0
    get=False
    for i in range(0,n):
        if(i+1<len(nums)):
            if(nums[i+1]-nums[i]>0):
                if(not get):
                    buyin.append(i)
                get=True
                money=money+nums[i+1]-nums[i]
            elif(nums[i+1]-nums[i]<0 and get):
                get=False
                buyout.append(i)
    if(get):
        buyout.append(n-1)
    result=[]
    for m in range(0,len(buyin)):
        result.append("("+str(buyin[m])+" "+str(buyout[m])+")")
    print(" ".join(result))
if __name__ == "__main__":
    total=int(input())
    for i in range(total):
        Test()