from collections import defaultdict


def find_longest(r, pre):
    if len(road[r]) == 0 or (len(road[r]) == 1 and road[r][0] == pre):
        return [0, r]
    else:
        choices = []
        for next_n in road[r]:
            if next_n != pre:
                choices.append(find_longest(next_n, r))
                choices[-1][0] += 1
        choices.sort()
        return choices[-1]


ns = int(input())
road = defaultdict(list)
while len(road) < ns:
    n1, n2 = map(int, input().split(' '))
    road[n1].append(n2)
    road[n2].append(n1)
longest1 = find_longest(list(road.keys())[0], 0)
longest2 = find_longest(longest1[1], 0)
print(longest2[0])
