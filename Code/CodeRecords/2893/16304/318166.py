def dealRes(arr):
    one=0
    two=0
    three=0
    count=0
    while count<len(arr):
        two|=one&arr[count]
        one^=arr[count]
        three=one&two
        one&=~three
        two&=~three
        count+=1
        
    print(one)


strs=input()
strs2=strs[1:-1]
numStr=strs2.split(",")
nums=list(map(int, numStr))
dealRes(nums)