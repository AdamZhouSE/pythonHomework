
test_cases = int(input())
for _ in range(test_cases):
    _ = input()
    data = list(map(int, list(filter(None, input().split(" ")))))
    length = len(data)
    lhs_counter = []
    rhs_counter = []
    for i in range(length):
        value = data[i]
        counter = 0
        for j in range(i-1, -1,-1):
            if data[i] <= data[j]:
                counter += 1
            else:
                break
        lhs_counter.append(counter)
        counter = 0
        for j in range(i+1, length):
            if data[i] <= data[j]:
                counter += 1
            else:
                break
        rhs_counter.append(counter)
    # print(lhs_counter)
    # print(rhs_counter)
    rst = []
    for i in range(0, length):
        rst.append(max([data[x] if (lhs_counter[x]+rhs_counter[x]>=i) else 0 for x in range(0, length)]))
    print(" ".join(map(str, rst)))