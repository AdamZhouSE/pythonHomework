import heapq

lists = eval("[" + input() + "]")
more = []
less = []

for num in lists:
    if num >= 0:
        more.append(num)
    else:
        less.append(num)

if len(lists) == 3:
    print(lists[0] * lists[1] * lists[2])
else:
    if len(more) == 0:
        result = heapq.nlargest(3, less)
        print(result[0] * result[1] * result[2])
    else:
        overZero = max(more)
        more.remove(overZero)
        if len(more) >= 2 and len(less) >= 2:
            result1 = heapq.nlargest(2, more)
            result2 = heapq.nsmallest(2, less)
            result = max(result1[0] * result1[1], result2[0] * result2[1])
        else:
            if len(more) >= 2:
                result1 = heapq.nlargest(2, more)
                result = (result1[0] * result1[1])
            else:
                result2 = heapq.nsmallest(2, less)
                result = result2[0] * result2[1]
        print(overZero * result)
