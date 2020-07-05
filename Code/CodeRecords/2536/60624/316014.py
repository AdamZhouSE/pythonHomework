import collections
def func19():
    in_str = input().strip()[1:-1]
    tickets = []
    while True:
        a = in_str.find("[")
        if a == -1:
            break
        end_ = in_str.find("]")
        temp = in_str[a+1:end_]
        in_str = in_str[end_+1:]
        i = temp.find("\"")
        temp = temp[i+1:]
        j = temp.find("\"")
        k = temp[:j]
        temp = temp[j+1:]
        i = temp.find("\"")
        temp = temp[i + 1:]
        j = temp.find("\"")
        l = temp[:j]
        tickets.append([k,l])
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
    print( s[::-1])
    return
func19()