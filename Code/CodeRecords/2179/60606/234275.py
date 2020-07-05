line1 = input().split(" ")
n = int(line1[0])
m = int(line1[1])
string = input()
for i in range(0, m):
    line2 = input().split(" ")
    floor1 = int(line2[0])
    floor2 = int(line2[2])
    ceil1 = int(line2[1])
    ceil2 = int(line2[3])
    sub1 = string[floor1-1:ceil1]
    sub2 = string[floor2-1:ceil2]
    sentinel = 0
    while True:
        if sentinel==len(sub1)-1 or sentinel==len(sub2)-1 or sub1[sentinel] != sub2[sentinel]:
            sentinel += 1
            break
        sentinel += 1
    print(sentinel)
    line2.clear()

