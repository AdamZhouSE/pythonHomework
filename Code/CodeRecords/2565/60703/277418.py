nums1 = [int(x) for x in input().split(",")]
nums2 = [int(x) for x in input().split(",")]
newList = (nums1+nums2)
newList.sort()
length = len(newList)
if(length%2==0):
    print(str((newList[length//2]+newList[(length//2)-1])/2)+"0000")
else:
    print(newList[length//2])