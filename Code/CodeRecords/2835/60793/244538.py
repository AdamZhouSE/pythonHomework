card_num = int(input())
cards = list(map(int, input().split(" ")))
cards.sort(reverse=True)
max_num = int("".join([str(x) for x in cards]))
if max_num == 555555555:
    print(-1)
else:
    print(max_num)
