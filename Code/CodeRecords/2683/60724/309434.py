T=int(input())
for k in range(T):
    string=input()
    result = []
    def DFS(nums, i):
        if i==len(string)-1:
            result.append(nums)
            return
        else:
            for j in range(i+1,len(string)):
                new_nums=nums[:]
                if string[j]>nums[-1]:
                    new_nums.append(string[j])
                DFS(new_nums,j)
    for i in range(len(string)):
        nums=[string[i]]
        DFS(nums,i)
    number=[]
    for i in range(len(result)):
        if len(result[i])>len(number):
            number=result[i]
    print(len(number))