def main():
    num_of_bugs, num_of_debugs = map(int, input().split(" "))
    graph = [[10000 for i in range(0, 2 ** num_of_bugs + 1)] for j in range(0, 2 ** num_of_bugs + 1)]
    solutions = []
    data = []
    for i in range(0, num_of_debugs):
        time, bn, fn = input().split(" ")
        data.append(time + " " + bn + " " + fn)
        weight = int(time)
        b1 = ""
        b2 = ""
        f1 = ""
        f2 = fn
        for j in range(0, num_of_bugs):
            if bn[j] == "0":
                b1 += "0"
                b2 += "0"
            elif bn[j] == "-":
                b1 += "0"
                b2 += "1"
            elif bn[j] == "+":
                b1 += "1"
                b2 += "0"
        for j in range(0, num_of_bugs):
            if fn[j] == "0":
                f1 += "0"
            elif fn[j] == "-":
                f1 += "1"
            elif fn[j] == "+":
                f1 += "0"
        solutions.append([weight, b1, b2, f1, f2])
    for i in range(2 ** num_of_bugs, 0, -1):
        for j in range(0, num_of_debugs):
            find_edge(i, solutions[j], graph)

    paths = shortest_path(2 ** num_of_bugs, 2 ** num_of_bugs, graph)
    if paths[1] == 10000:
        print(0)
    else:
        print(paths[1])


def find_edge(num, solution, graph):
    b1 = solution[1]
    b2 = solution[2]
    f1 = solution[3]
    f2 = solution[4]
    length = len(b1)
    if convert_bin(logic_operation(logic_negate(convert_int(num, length)), b1)) != 0:
        return None
    if convert_bin(logic_operation(convert_int(num, length), b2)) != 0:
        return None
    if convert_bin(logic_operation(convert_int(num, length), f1)) == 0:
        return None
    bin_num = convert_int(num, length)
    bin_next_num = ""
    for i in range(0, length):
        if f2[i] == "0":
            bin_next_num += bin_num[i]
        elif f2[i] == "-":
            bin_next_num += "0"
        elif f2[i] == "+":
            bin_next_num += "1"
    next_num = convert_bin(bin_next_num)
    graph[num + 1][next_num + 1] = solution[0]
    graph[next_num + 1][num + 1] = solution[0]
    return next_num


def convert_int(num, length):
    result = ""
    for i in range(0, length):
        if num > 0:
            result = str(num % 2) + result
            num = int((num - num % 2) / 2)
        else:
            result = "0" + result
    return result


def convert_bin(string):
    temp = list(reversed(string))
    result = 0
    for i in range(0, len(string)):
        result += int(temp[i]) * (2 ** i)
    return result


def logic_operation(s1, s2):
    result = ""
    for i in range(0, len(s1)):
        result += str(int(s1[i]) & int(s2[i]))
    return result


def logic_negate(string):
    result = ""
    for i in range(0, len(string)):
        if string[i] == "0":
            result += "1"
        else:
            result += "0"
    return result


def shortest_path(n, start, graph):
    times = [10000] * (n + 1)
    able_to_change = [True] * (n + 1)
    past = [start for a in range(n + 1)]
    for j in range(1, n + 1):
        times[j] = graph[start][j]
    able_to_change[start] = False

    for j in range(1, n):
        next_point = 0
        for k in range(1, n):
            if able_to_change[k] and times[k] != 10000:
                if next_point == 0:
                    next_point = k
                else:
                    if times[k] < times[next_point]:
                        next_point = k
        able_to_change[next_point] = False
        for k in range(1, n + 1):
            if able_to_change[k] and times[k] > times[next_point] + graph[next_point][k]:
                times[k] = times[next_point] + graph[next_point][k]
                past[k] = next_point

    return times


if __name__ == '__main__':
    main()
