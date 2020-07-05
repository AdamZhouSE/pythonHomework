def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    k=int(input())
    nums.sort()
    result=[]
    i=0
    while(i<len(nums)):
        temp=nums[i]
        try:
            nums.remove(temp)
            nums.remove(k-temp)
            result.append([temp,k-temp])
        except:
            i=i+1
    if(not result):
        print(-1)
    else:
        for x in result:
            print(str(x[0])+" "+str(x[1])+" "+str(k))
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()