test_num = int(input())
for i in range(test_num):
    sentinel = 0
    line1 = input().split(" ")
    line2 = input().split(" ")
    n = int(line1[0])
    x = int(line1[1])
    line2 = [int(y) for y in line2]
    for j in range(len(line2)):
        for k in range(j+1,len(line2)):
            if x == line2[j] + line2[k]:
                print("Yes")
                sentinel = 1
                break
        if sentinel == 1:
            break
    if sentinel != 1:
        print("No")
