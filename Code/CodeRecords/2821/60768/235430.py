cards = int(input())
values = input().split(' ')
values = [int(x) for x in values]
s_sum = 0
d_sum = 0

for i in range(cards // 2 + 1):
    if values[0] > values[len(values) - 1]:
        s_sum = s_sum + values[0]
        values.pop(0)
    else:
        s_sum = s_sum + values[len(values) - 1]
        values.pop()
    if len(values) == 0:
        break

    if values[0] > values[len(values) - 1]:
        d_sum = d_sum + values[0]
        values.pop(0)
    else:
        d_sum = d_sum + values[len(values) - 1]
        values.pop()
    if len(values) == 0:
        break

print(str(s_sum) + " " + str(d_sum))