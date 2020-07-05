def tell(frinend: list, know: list, talker: int):
    know[talker] = 0
    if frinend[talker]:
        for i in frinend[talker]:
            if know[i] == 1:
                know[i] = 0
                tell(frinend, know, i)


def play(friend: list, know: list, hasfriend: set, arr: list, money: int, ans: list):
    if sum(know) == 0:
        ans[0] = min(ans[0], money)
    else:
        for i in hasfriend:
            if know[i] == 1:
                tem = know[:]
                tell(friend, tem, i)
                play(friend, tem,hasfriend, arr, money + arr[i], ans)


def func38():
    arr = list(map(int, input().split()))
    n, m = arr[0], arr[1]
    arr = list(map(int, input().split()))
    if m == 0:
        print(sum(arr))
    else:
        
        know = [1 for i in range(0, n)]
        friend = [[] for i in range(0, n)]
        hasfriend = set()
        for i in range(0, m):
            res = list(map(int, input().split()))
            friend[res[1] - 1].append(res[0] - 1)
            friend[res[0] - 1].append(res[1] - 1)
            hasfriend.add(res[0] - 1)
            hasfriend.add(res[1] - 1)
        nofriend = {i for i in range(0, n)} - hasfriend
        money = 0
        for item in nofriend:
            money += arr[item]
            know[item] = 0
        ans = [sum(arr)]
        play(friend, know, hasfriend, arr, money, ans)
        print(ans[0])


func38()
