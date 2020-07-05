n = int(input())
for i in range(n):
    input()
    string = input().replace(" ", "")
    count = 0
    for i in string:
        count += int(i)
    if count % 3 == 0:
        print(1)
    else:
        print(0)