def Test():
    s=int(input())
    nums=bin(s)[2:]
    a=[]
    b=[]
    i=-1
    result=""
    if(len(nums)%2==1):
        nums="0"+nums
    while(i>=-len(nums)):
        if(i%2==0):
            b.append(nums[i])
        else:
            a.append(nums[i])
        i=i-1
    for i in range(0,len(b)):
        result=result+b[i]
        result=result+a[i]
    result=result[::-1]
    print(int(("0b"+result),2))

if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()