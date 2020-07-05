def func6():
    ans1 = [0, 0]
    ans2 = [0, 0]
    for _ in range(0, eval(input())):
        res = list(map(int, input().split()))
        if res[0] == 1:
            ans1[0] += res[1]
            ans1[1] += res[2]
        else:
            ans2[0] += res[1]
            ans2[1] += res[2]
    if ans1[0] >= ans1[1]:
        print("LIVE")
    else:
        print("DEAD")
    if ans2[0] >= ans2[1]:
        print("LIVE")
    else:
        print("DEAD")


func6()