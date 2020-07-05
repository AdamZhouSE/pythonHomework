def permutations(li, s, l):
    if s == l:
        permutation.append("".join(li))

    else:
        temp = list.copy(li)
        for index in range(s, l):
            temp[index], temp[s] = temp[s], temp[index]
            permutations(temp, s + 1, l)


a = input()
num = list(a)
permutation = []
permutations(num, 0, len(num))
y = 0
for i in range(len(permutation)):
    if permutation[i][0] == "0":
        list.pop(permutation, i)
for i in range(len(permutation)):
    x = int(permutation[i])
    if x == 1:
        print("true")
        y = 1
    while x % 2 == 0:
        x = x / 2
        if x == 1:
            print("true")
            y = 1
if y == 0:
    print("false")