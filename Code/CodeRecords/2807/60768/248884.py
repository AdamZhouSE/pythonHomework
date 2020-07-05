s = input()
case = input().split(' ')
key = input().split(' ')
case = [int(x) for x in case]
key = [int(x) for x in key]
open = 0
odd = []
non_odd = []
for e in key:
    if e % 2 == 0:
        non_odd.append(e)
    else:
        odd.append(e)
for e in case:
    if e % 2 == 0 and len(odd) != 0:
        open += 1
        odd.pop()
    if e % 2 == 1 and len(non_odd) != 0:
        open += 1
        non_odd.pop()
print(open)