import bisect
def findBestValue(arr, target):
        if sum(arr)<=target:
            return max(arr)
        part1=[]
        part2=[]
        for a in arr:
            if a<=target/len(arr):
                part1.append(a)
            else:
                part2.append(a)
        while part1:
            target-=sum(part1)
            tmp=part2
            part1=[]
            part2=[]
            for a in tmp:
                if a<=target/len(tmp):
                    part1.append(a)
                else:
                    part2.append(a)
        return target//len(part2) if target%len(part2)<=len(part2)/2 else target//len(part2)+1





    
info=input().split(',')
a=[int(y) for y in info]
arr=[]
for i in range(len(a)-1):
    arr.append(a[i])
target=a[-1]
print(findBestValue(arr,target))