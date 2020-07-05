card_num = int(input())
cards = list(map(int, input().split(" ")))
cards.sort(reverse=True)
result = -1
if cards[0] == 0:
    print(0)
max_num = int("".join([str(x) for x in cards]))
fives = cards.count(5)
zeros = cards.count(0)
upper_times = int(max_num / 90) + 1
for i in range(0, upper_times):
    temp_ls = list(str(90 * i))
    if temp_ls.count('5') <= fives and temp_ls.count('0') <= zeros:
        result = 90 * i
print(result)    
