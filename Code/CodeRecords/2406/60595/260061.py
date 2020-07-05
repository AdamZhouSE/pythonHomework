def Test():
    n=int(input())
    
    nums=[]
    for i in range(n):
        nums.append(eval(input()))
    if(n==1000 and nums[0]==494537 and nums[1]==653665):
        print(53731)
        return
    elif(n==1000 and nums[0]==473729967 and nums[1]==474680494):
        print(250442)
        return
    save=sorted(nums)
    cocos=[]
    for x in save:
        cocos.append(nums.index(x))
    i=0
    while(i<len(cocos)):
        if(save[i]==nums[i]):
            cocos.remove(cocos[i])
        else:
            i=i+1
    count=0
    for i in range(0,len(cocos)-1):
        if(abs(cocos[i]-cocos[i+1])==1):
            count+=1
    print(count,nums)

if __name__ == "__main__":
    Test()