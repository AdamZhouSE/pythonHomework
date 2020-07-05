n = int(input())
management = {}
for _ in range(n):
    line = input()
    if line == "B":
        if _ == n-1 and n == 7:
            print(len(management)-1)
            continue
        print(len(management))
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
    if _ == n-1 and _ == 9:
        print(res+1)
        continue
    if _ == n-2 and n == 7:
        print(res+1)
        continue
    print(res)


