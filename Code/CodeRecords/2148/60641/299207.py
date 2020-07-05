def main():
    n = int(input())
    for i in range(0, n):
        num_of_facilities, num_of_roads, gap = map(int, input().split(" "))
        goods = [10000] + list(map(int, input().split(" ")))
        num_of_cola = 0
        num_of_burger = 0
        graph = [[10000 for a in range(num_of_facilities + 1)] for b in range(num_of_facilities + 1)]
        for j in range(0, num_of_roads):
            x, y, time = map(int, input().split(" "))
            graph[x][y] = time
            graph[y][x] = time
        start, end = map(int, input().split(" "))

        times = [10000] * (num_of_facilities + 1)
        able_to_change = [True] * (num_of_facilities + 1)
        past = [start for a in range(num_of_facilities + 1)]
        for j in range(1, num_of_facilities + 1):
            times[j] = graph[start][j]
        able_to_change[start] = False

        for j in range(1, num_of_facilities):
            next_facility = 0
            for k in range(1, num_of_facilities + 1):
                if able_to_change[k] and times[k] != 10000:
                    if next_facility == 0:
                        next_facility = k
                    else:
                        if times[k] < times[next_facility]:
                            next_facility = k
            able_to_change[next_facility] = False
            for k in range(1, num_of_facilities + 1):
                if able_to_change[k] and times[k] > times[next_facility] + graph[next_facility][k]:
                    times[k] = times[next_facility] + graph[next_facility][k]
                    past[k] = next_facility

        now_facility = end
        path = []
        result = times[end]
        while now_facility != start:
            path.insert(0, now_facility)
            now_facility = past[now_facility]
        path.insert(0, start)
        for j in range(0, len(path)):
            if goods[path[j]] == 1:
                num_of_cola += 1
            else:
                num_of_burger += 1
            if max(num_of_cola, num_of_burger) - min(num_of_cola, num_of_burger) > gap:
                result = -1
                break
        print(result)


if __name__ == '__main__':
    main()
