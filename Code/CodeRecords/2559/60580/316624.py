num = int(input())
for i in range(num):
    string = input()
    flag = False
    for j in range(len(string)):
        if string.count(string[j]) > 1:
            flag = True
            print(0)
            break
    if not flag:
        print(1)
