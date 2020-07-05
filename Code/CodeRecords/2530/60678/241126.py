s = input()
d = input()

outcome = ''


def findANDappendANDdel(character):
    global s
    global d
    global outcome
    position = d.find(character)

    while position != -1:
        d =list(d)
        outcome = outcome + character
        del d[position]
        d = ''.join(d)
        position = d.find(character)

for i in s:
    findANDappendANDdel(i)

print(outcome+d)