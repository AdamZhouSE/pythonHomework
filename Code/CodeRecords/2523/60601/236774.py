import collections

def solve(mat):
    r, c = len(mat), len(mat[0])
    data = collections.defaultdict(list)

    for i in range(r):
        for j in range(c):
            data[i - j].append(mat[i][j])

    for i in data:
        data[i].sort()

    for i in range(r):
        for j in range(c):
            mat[i][j] = data[i - j].pop(0)
    return mat


if __name__ == '__main__':
    line = input()
    line = line[2:len(line) - 2]
    line = line.split('],[')
    for i in range(len(line)):
        line[i] = line[i].replace(',', ' ')
        line[i] = list(map(int, line[i].split()))
    #print(line)
    print(solve(line))
