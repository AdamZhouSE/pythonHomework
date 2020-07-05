
def solve(row):
    n_swap = 0
    place = {x: i for (i, x) in enumerate(row)}
    n = len(row)
    for i in range(0, n, 2):
        x = row[i]
        if x % 2 == 0:
            y = x + 1
        else:
            y = x - 1
        j = place[y]

        if abs(i - j) > 1:
            row[i + 1], row[j] = row[j], row[i + 1]
            place[row[i + 1]], place[row[j]] = i + 1, j
            n_swap += 1
    return n_swap
if __name__ == '__main__':
    line = input()
    line = line[1:len(line) - 1]
    line = line.replace(',', ' ')
    #print(line)
    num = list(map(int, line.split()))
    #print(num)
    print(solve(num))