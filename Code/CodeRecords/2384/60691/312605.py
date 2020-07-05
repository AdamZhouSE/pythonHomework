def function(l):
    for i in range(1, len(l)+2):
        if i not in l:
            return i


n = int(input())
nums = []
string = []

for i in range(n):
    nums.append(int(input()))
    string.append(input())

for i in range(n):
    ltemp = list(map(int, string[i].split(' ')))
    print(function(ltemp))


