lists = list(map(int, input().split(",")))
toFind = int(input())
if lists.__contains__(toFind):
    print(lists.index(toFind))
else:
    print(-1)