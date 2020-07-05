times = input()
for i in range(int(times)):
    length = int(input())
    list = sorted(input().split(' '))
    for j in range(len(list)//2+1):
        out = -1
        if j+len(list)//2 > len(list)-1:
            break
        if list[j]==list[j+len(list)//2]:
            out = list[j]
            break
    print(out)