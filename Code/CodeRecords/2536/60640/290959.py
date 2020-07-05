def find_itinerary(tickets):
    from collections import defaultdict
    dest = defaultdict(list)
    for k, v in sorted(tickets)[::-1]:
        dest[k] += v,
    res = list()
    stack = ['JFK']
    while stack:
        while dest[stack[-1]]:
            stack.append(dest[stack[-1]].pop())
        res.append(stack.pop())
    return res[::-1]


inp = eval(input())
ans = find_itinerary(inp)
print(ans)
