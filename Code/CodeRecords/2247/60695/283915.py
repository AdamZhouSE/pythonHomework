a = input().split(",")
alex = 0
lee = 0
round = 1
while len(a) > 0:
    if int(a[0]) >= int(a[len(a) - 1]):
        pick = int(a[0])
        a.remove(a[0])
    else:
        pick = int(a[len(a) - 1])
        a.remove(a[len(a) - 1])
    if round % 2 == 1:
        alex += pick
    else:
        lee += pick
    round += 1
print(alex > lee)