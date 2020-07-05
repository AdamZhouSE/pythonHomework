n=int(input())
for i in range(n):
    string=input()
    length=len(string)
    nums=[1]*length
    for j in range(1,length):
        for k in range(j):
            if string[j]>string[k] and nums[j]<nums[k]+1:
                nums[j]=nums[k]+1
    print(max(nums))
            
            