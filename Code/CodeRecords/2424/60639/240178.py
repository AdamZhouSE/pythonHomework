T = int(input())
for i in range(T):
    n=int(input())
    inp=input().split(' ')
    nums=[]
    for i in range(n):
        nums.append(int(inp[i]))
    exist=0
    for j in range(n):
        num=nums[j]
        if (nums.count(num))%2!=0:
            print(num)
            exist=1
            break
        else:
            continue
    if exit==0:
        print(0)
    else:
        break