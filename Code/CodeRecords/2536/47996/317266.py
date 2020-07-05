import collections
def findItinerary(tickets):
    d = collections.defaultdict(list)
    for f, t in tickets:
        d[f] += [t]
    for f in d:
        d[f].sort()
    ans = []
    def dfs(f):
        while d[f]:
            dfs(d[f].pop(0))
        ans.insert(0, f)
    dfs('JFK')
    return ans
str = input()
judge = True
if str[8] == " ":
    judge = False
    str = str[1:-2].split("], ")
else:
    str = str[1:-2].split("],")
tickets = []
for item in str:
    item = item[1:].replace('"',"")
    if judge:
        temp = item.split(",")
    else:
        temp = item.split(", ")
    tickets.append(temp)
print(findItinerary(tickets))
