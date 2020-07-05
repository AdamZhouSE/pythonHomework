questNum = int(input())

for quest in range(questNum):
    s = input()

    sum = 0
    for i in range(len(s) - 2):
        if s[i: i + 3] == "012" or s[i: i + 3] == "021" or s[i: i + 3] == "102" or s[i: i + 3] == "120" or s[i: i + 3] == '210' or s[i: i + 3] == "201":
            sum += 1

    print(sum)