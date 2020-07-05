"""
这里有 n 个航班，它们分别从 1 到 n 进行编号
我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位
请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数
"""

m=int(input())

bookings=[]
for i in range(m):
    bookings.append(eval("["+str(input())+"]"))

n=int(input())
answer=[int(0) for i in range(n)]

for i in range(m):
    begin=bookings[i][0]
    end=bookings[i][1]
    seat=bookings[i][2]
    while(begin<=end):
        answer[begin-1]+=seat
        begin+=1

print("[",end="")
for i in range(n-1):
    print(str(answer[i])+", ",end="")
print(str(answer[n-1])+"]")