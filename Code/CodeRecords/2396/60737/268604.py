n = int(input())
nums = [int(i) for i in input().split( )]
ret = []
for i in range(n):
    temp = nums[i:]
    ind = temp.index(min(temp))
    ret.append(ind+i+1)
    ex = temp[:ind+1]
    ex.reverse()
    nums = nums[:i]+ex+temp[ind+1:]
for j in ret:
    print(j,end=" ")
