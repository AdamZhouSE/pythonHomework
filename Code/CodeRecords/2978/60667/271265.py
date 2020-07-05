li = input().split()
for i in range(len(li[0])):
    if li[0][i] != li[1][i]:
        print(ord(li[0][i]) - ord(li[1][i]))
        quit()