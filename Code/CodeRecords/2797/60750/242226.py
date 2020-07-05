
def watchMoon():
    days = int(input())
    size = list(map(int,input().split(' ')))
    if size[days - 1] == 0:
        print('UP')
        return
    if days <= 1:
        print(-1)
        return
    if size[days - 1] == 15:
        print('DOWN')
        return
    if size[days - 1] > size[days - 2]:
        print('UP')
        return
    print('DOWN')
    return

watchMoon()