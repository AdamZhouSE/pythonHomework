n = int(input())
x = input().strip().split()
li = []
for i in x:
    li.append(int(i))
li = sorted(li)

m = int(input())
commands = []
for i in range(m):
    commands.append(input())

for i in commands:
    if i[0:3] == "add":
        tar = int(i[4:].strip())
        if len(li) == 1:
            li.append(tar)
        else:
            idx = 0
            while idx < len(li)-1  and (tar < li[idx] or tar > li[idx+1]):
                idx += 1
            li.insert(idx+1, tar)
        # print(li)
    else:
        if len(li) % 2 == 1:
            print(li[len(li)//2])
        else:
            print(min(li[len(li)//2], li[len(li)//2-1]))
