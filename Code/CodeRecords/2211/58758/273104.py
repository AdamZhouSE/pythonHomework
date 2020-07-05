n, k = [int(x) for x in input().split()]
madams = ['']
for i in range(n):
    queen = input().split()
    first_name = queen[0]
    mother = int(queen[1])
    name = first_name+madams[mother]
    madams.append(name)
ans = []
for i in range(k):
    string = input()
    count = 0
    for madam in madams:
        if madam[0: len(string)] == string:
            count += 1
    ans.append(count)
for i in ans:
    print(i)
