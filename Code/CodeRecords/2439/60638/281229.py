def find(numbers,n):
    for i in range(0,len(numbers)):
        if numbers[i][0]==n:
            return i
def check(begin,end,res,numbers):
    if begin==end:
        return res
    else:
        i=find(numbers,begin)
        begin=numbers[i][1]
        return check(begin,end,res,numbers)^numbers[i][2]

n=int(input())
numbers=[]
for x in range(0,n-1):
    numbers.append(list(map(int,input().split(" "))))
m=int(input())
nums=[]
for x in range(0,m):
    nums.append(list(map(int,input().split(" "))))
for i in range(0,m):
    res=0
    begin=nums[i][0]
    end=nums[i][1]
    res=check(begin,end,res,numbers)
    print(res)