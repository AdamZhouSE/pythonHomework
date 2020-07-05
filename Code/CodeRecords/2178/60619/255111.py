t = int(input())
numbers = input().strip().split(" ")
string = []
subs = []
result = 0
for i in range(t):
    string.append(int(numbers[i]))
    if i == 0:
        result = 1
        subs.append([int(numbers[i])])
        print(result)
    else:
        for j in range(len(string)):
            if string[j:] not in subs:
                subs.append(string[j:])
        result = len(subs)
        print(result)