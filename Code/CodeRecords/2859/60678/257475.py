def judge():
    times = int(input())
    chart = []
    characters = []
    for i in range(0, times):
        row = input()
        chart.append(row)
    characters.append(chart[0][0])
    characters.append(chart[0][1])
    if characters[0] == characters[1]:
        return 'NO'
    for row in chart:
        for char in row:
            if char != characters[0] and char != characters[1]:
                return 'NO'

    for i in range(0, times):
        for j in range(0, times):
            if i == j or i == times - j - 1:
                if chart[i][j] != characters[0]:
                    return "NO"
            else:
                if chart[i][j] != characters[1]:
                    return "NO"
    return "YES"


if __name__ == '__main__':
    print(judge())