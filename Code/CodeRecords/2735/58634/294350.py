n,m = map(int,input().split(" "))
temp = input().strip()
nums = [int(i) for i in temp.split(" ")]
for _ in range(m):
    start,end,k = map(int,input().split(" "))
    start -=1
    end -=1
    temp = []
    for i in range(start,end+1):
        temp.append(nums[i])
    temp.sort()
    print(temp[k-1])