card_num = int(input())
cards = list(map(int, input().split(" ")))
cards.sort(reverse=True)
max_num = int("".join([str(x) for x in cards]))
print(max_num)   