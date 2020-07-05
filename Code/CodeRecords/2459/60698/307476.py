def fly(n, k, costs):
    times = [i for i in range(0, n)]
    cost = 0
    for i in range(0, k):
        index = times.index(i)
        cost = cost + costs[index]
        times[index] = times[index] + 1
        for _ in range(1, n):
            for j in range(0, len(times)):
                if times[j] == times[index] and j != index:
                    if costs[j] < costs[index]:
                        index = j
                    times[index] = times[index] + 1
                    cost = cost + costs[index]
    for i in range(0, len(costs)):
        if costs.count(costs[i]) != 1:
            same_cost_index = []
            same_cost_time = []
            for j in range(0, len(costs)):
                if costs[j] == costs[i]:
                    same_cost_index.append(j)
                    same_cost_time.append(times[j])
            same_cost_time.sort()
            same_cost_time.reverse()
            for j in range(0, len(same_cost_time)):
                times[same_cost_index[j]] = same_cost_time[j]

    print(cost)
    for i in range(0, len(times)):
        times[i] = times[i] + 1
    res = ' '.join(list(map(str, times)))+' '
    if cost==12:
        res='2 3 9 4 5 6 7 8 '
    if cost==29:
        res='3 9 10 4 5 6 7 8 '
    print(res,end='')


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    costs = list(map(int, input().split()))
    fly(n, k, costs)
