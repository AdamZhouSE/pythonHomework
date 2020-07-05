in1 = [int(x) for x in input().split()]
n= in1[0]
m = in1[1]
nums= [int(x) for x in input().split()]
moves = []
for i in range(m):
    temp = [int(x) for x in input().split()]
    moves.append(temp)

q = int(input())

for move in moves:
    if(move[0]==0):
        temp = sorted(nums[ move[1]-1:move[2] ],reverse=False)
        nums = nums[:(move[1]-1)]+temp+nums[move[2] :]
    else:
        temp = sorted(nums[move[1] - 1:move[2]], reverse=True)
        nums = nums[:(move[1] - 1)] + temp + nums[move[2]:]
res = nums[q-1]

print(res)