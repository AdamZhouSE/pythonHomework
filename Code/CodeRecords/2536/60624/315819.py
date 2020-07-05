def func19():
    in_str = input().strip()[1:-1]
    tickets = []
    while True:
        start = in_str.find("[")
        if start == -1:
            break
        end_ = in_str.find("]")
        temp = in_str[start+1:end_].split(", ")
        in_str = in_str[end_+1:]
        tickets.append([temp[0][1:-1],temp[1][1:-1]])
    paths = collections.defaultdict(list)
    for start, tar in tickets:
        paths[start].append(tar)
    for start in paths:
        paths[start].sort(reverse=True)
    s = []

    def search(start):
        while paths[start]:
            search(paths[start].pop())
        s.append(start)

    search("JFK")
    print(s[::-1])
    return
func19()