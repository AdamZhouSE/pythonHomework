nums = list(map(int, input().split(",")))
N = len(nums)
total = 0
for num in nums:
    total += num
average = total/N
finish = False
for i in range(1, pow(2,N)-1):
    binary = bin(i).replace("0b", "")
    temp = 0
    count = 0
    while len(binary) < N:
        binary = "0"+binary
    for k in range(N):
        if binary[k] == "1":
            count += 1
            temp+=nums[k]
    if temp/count == average:
        print(True)
        finish = True
        break
if not finish:
    print(False)
