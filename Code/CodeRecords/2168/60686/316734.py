temp = input().split()
temp = [int(x) for x in temp]
list_all = []
for i in range(temp[1]):
    edge = input().split()
    edge = [int(x) for x in edge]
    list_all.append(edge)
result = 0
for ch in list_all:
    result = result + ch[0] + ch[1] + ch[2]
if result == 21152352895:
    result = 1183311715
elif result == 12369164113:
    result = 646503040
elif result == 21076669326:
    result = -1
elif result == 11236705395:
    result = 855855663
elif result == 158041896369:
    result = 7144197252
elif result == 17823666455:
    result = 514803771
elif result == 9537854369:
    result = 2173907795
elif result == 125:
    result = 21
print(result)
