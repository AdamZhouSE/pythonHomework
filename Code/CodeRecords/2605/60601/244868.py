import heapq
def add(list1:list,list2:list):
    for i in list2:
        heapq.heappush(list1,i)
    #list1.sort()
    return list1
def find(x:int,num:list):
    for i in range(len(num)):
        for j in range(len(num[i])):
            if num[i][j]==x:
                return i
    return -1

if __name__=='__main__':
    line = input().split(' ')
    N = int(line[0])
    M = int(line[1])
    nums = list(map(int,input().split(' ')))
    numMap = list(nums)
    for i in range(len(nums)):
        nums[i] = [nums[i]]
    for i in range(M):
        order = list(map(int,input().split(' ')))
        if order[0]==1:
            x = order[1]
            y = order[2]
            if find(numMap[x-1],nums)!=-1 and find(numMap[y-1],nums)!=-1:
                if find(numMap[x-1],nums)!=find(numMap[y-1],nums):
                    Hx = nums[find(numMap[x-1],nums)]
                    Hy = nums[find(numMap[y-1],nums)]
                    H = add(Hx,Hy)
                    nums.remove(Hx)
                    nums.remove(Hy)
                    nums.append(H)
        else:
            x = order[1]
            if find(numMap[x-1],nums)!=-1:
                j = find(numMap[x-1],nums)
                print(nums[j][0])
                nums[j] = nums[j][1:]
                pass
            else:print(-1)


