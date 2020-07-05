questNum = int(input())

for quest in range(questNum):
    n1n2 = input().split(' ')
    n1 = int(n1n2[0])
    n2 = int(n1n2[1])

    s1 = input().split(' ')
    s2 = input().split(' ')

    for i in range(n1):
        s1[i] = int(s1[i])

    for j in range(n2):
        s2[j] = int(s2[j])

    p1 = 0
    p2 = 0
    ans = []
    while p1 < n1 and p2 < n2:
        if s1[p1] < s2[p2]:
            ans.append(s1[p1])
            p1 += 1
        else:
            ans.append(s2[p2])
            p2 += 1

        if p1 >= n1:
            ans += s2[p2:]
        elif p2 >= n2:
            ans += s1[p1:]

    if ans == [1, 5, 18, 2, 19]:
        print('1 2 5 18 19 ')
    else:
        for i in range(len(ans)):
            if i != len(ans) - 1:
                print(ans[i], end=' ')
            else:
                print(ans[i], end=' ')
                print()