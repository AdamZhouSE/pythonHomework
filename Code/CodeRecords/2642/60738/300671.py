num_list=list(map(int,input().split(",")))
num_list.sort()
i, n = 0, len(num_list)
min_moves = n
max_moves = max(num_list[-1]-num_list[1], num_list[-2]-num_list[0])-n+2
for j in range(n):
    while num_list[j]-num_list[i] >= n:
        i += 1
        if j-i+1 == n-1 and num_list[j]-num_list[i]==n-2:
            min_moves = min(2, min_moves)
        else:
            min_moves = min(min_moves, n-(j-i+1))
prin([min_moves, max_moves])
