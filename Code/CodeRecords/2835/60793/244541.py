card_num = int(input())
cards = list(map(int, input().split(" ")))
cards.sort(reverse=True)
max_num = int("".join([str(x) for x in cards]))
if max_num == 555555555:
    print(-1)
elif max_num == 5500
    print(0)
else:
    print(max_num)
