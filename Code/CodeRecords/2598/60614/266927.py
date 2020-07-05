init=[int(x) for x in input().split()]
numOfOperation=init[0]
moShu=init[1]
t=0
nums=[]
for i in range(numOfOperation):
    operation=input().split()
    if operation[0]=='A':
        n=int(operation[1])
        nums.append((n+t)%moShu)
    else:
        l=int(operation[1])
        temp=nums[len(nums)-l:]
        temp.sort(reverse=True)
        t=temp[0]
        print(t)