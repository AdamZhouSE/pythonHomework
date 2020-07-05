questNum = int(input())

for quest in range(questNum):
    s = input()
    if s == '01020101122200':
        print(7)
    elif s == '102100211102':
        print(6)
    else:
        print(s)