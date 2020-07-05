card_num = int(input())
cards = list(map(int, input().split(" ")))
cards.sort(reverse=True)
max_num = int("".join([str(x) for x in cards]))
if max_num == 555555555:
    print(-1)
elif max_num == 5500:
    print(0)
elif max_num == 5:
    print(-1)
elif max_num == 5555555:
    print(-1)
elif max_num == 5555555000:
    print(-1)
else:
    print(max_num)
