n = int(input())
nums = [4,8,15,16,23,42]
times = [0]*6
result = 0
for i in [int(i) for i in input().split(" ")]:
    temp = nums.index(i)
    if not temp or times[temp-1] > times[temp]:
        times[temp] +=1
    else:
        result+=1
result+=sum(i-times[-1] for i in times)
print(result)