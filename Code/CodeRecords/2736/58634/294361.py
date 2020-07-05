n,m = map(int,input().split(" "))
nums = [int(i) for i in input().split(" ")]
for _ in range(m):
    line = input().split(" ")
    if line[0] == "Q":
        start = int(line[1])-1
        end = int(line[2])-1
        k = int(line[3])
        temp = []
        for i in range(start,end+1):
            temp.append(nums[i])
        temp.sort()
        print(temp[k-1])
    else:
        index = int(line[1])-1
        new = int(line[2])
        nums[index] = new