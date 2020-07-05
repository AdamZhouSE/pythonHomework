def findUnsortedSubarray(nums):
        afterNums=nums[:]
        afterNums.sort()

        l=0
        r=len(nums)-1

        while nums[l]==afterNums[l]:
            if l==r:
                print(0)
                return
            l+=1
        
        while nums[r]==afterNums[r]:
            if l==r:
                print(0)
                return
            r-=1
        
        print(r-l+1)
    
a=input()
a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))
findUnsortedSubarray(l)
