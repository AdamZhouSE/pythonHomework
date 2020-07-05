count = int(input())
for n in range(count):
    info = input().split()
    num = int(info[0])
    tar = int(info[1])
    array = [int(x) for x in input().split()]
    repo=[]
    for a in array:
        div=tar/a
        if div in repo:
            print("Yes")
            break
        repo.append(a)
    else:
        print("No")
    