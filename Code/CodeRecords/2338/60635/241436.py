nums=int(input())
for i in range(nums):
    info=input().split()
    n=int(info[0])
    tar=int(info[1])
    array=[int(x) for x in input().split()]
    diff=0
    flag=0
    repo=[]
    for a in array:
        diff=tar-a
        if diff in repo:
            print("Yes")
            break
        repo.append(a)
    else:
        print("No")