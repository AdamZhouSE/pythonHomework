def find_ans(array, query):
    min_age = 200001
    for ii in range(len(array)):
        if int(array[ii][1]) <= int(query[1]) and int(array[ii][2]) >= int(query[2]):
            curr_age = int(array[ii][2])
            if min_age > curr_age:
                min_age = curr_age
    if min_age == 200001:
        return -1
    else:
        return min_age


inp = input().split(" ")
N, Q = int(inp[0]), int(inp[1])
current = []
for i in range(Q):
    inp = input().split(" ")
    if inp[0] == 'M':
        current.append(inp)
    else:
        res = find_ans(current, inp)
        print(res)
