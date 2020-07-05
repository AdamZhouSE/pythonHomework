if __name__ == '__main__':
    num, gap = map(int, input().split(" "))
    costs = [0] + list(map(int, input().split(" ")))
    able_to_cost = [True for i in range(0, num + 1)]
    cost = 0
    result = [0 for i in range(0, num + 1)]
    for i in range(1 + gap, 1 + num + gap):
        plane = 0
        for j in range(1, min(i + 1, num + 1)):
            if plane == 0 and able_to_cost[j]:
                plane = j
            else:
                if costs[j] >= costs[plane] and able_to_cost[j]:
                    plane = j
        able_to_cost[plane] = False
        result[plane] = i
        cost += (i - plane) * costs[plane]
    print(cost)
    print(" ".join(map(str, result[1:])) + " ", end="")

