if __name__ == '__main__':
    n = int(input())
    res = [-1] * n
    sections = []
    for i in range(n):
        sections.append([int(j) for j in input().split(',')])
    for i in range(n):
        for j in range(n):
            if sections[j][0] >= sections[i][1]:
                if res[i] == -1:
                    res[i] = j
                else:
                    if sections[j][0] < sections[res[i]][0]:
                        res[i] = j
    print(res)