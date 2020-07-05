lists = list(map(int, input().split(",")))
lists.sort()
ans = lists[lists.__len__()-1]*lists[lists.__len__()-2]*lists[lists.__len__()-3]
print(ans)