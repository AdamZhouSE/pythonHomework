nums=list(map(int,input().split(" ")))
strings=[]
for i in range(0,nums[0]):
    strings.append(input())
numbers=[]
for i in range(0,nums[1]):
    numbers.append(list(map(int,input().split(" "))))
for i in range(0,nums[1]):
    lists=strings[numbers[i][0]-1:numbers[i][1]]
    lists.sort()
    print(lists[-1])