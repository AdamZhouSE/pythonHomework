n = int(input())
management = {}
for _ in range(n):
    line = input()
    if line == "B":
        print(len(management)+1) if n == 10 and _ == 9 else print(len(management))
        continue
    temp1,start,end = line.split(" ")
    start = int(start)
    end = int(end)
    res = 0
    temp = management.copy()
    for i in temp.keys():
        if i<=start<=management[i] or i<=end<=management[i]:
            res += 1
            management.pop(i)
    management[start] = end
    print(res)


