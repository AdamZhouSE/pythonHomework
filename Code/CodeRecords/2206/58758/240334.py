count = int(input())
ans = []
for i in range(0, count):
    n = int(input())
    the_sum = 0
    for j in range(1, n+1):
        this_num = 1
        start = j * (j-1) // 2 + 1
        for k in range(start, start+j):
            this_num *= k
        the_sum += this_num
    ans.append(the_sum)
for i in ans:
    print(i)
