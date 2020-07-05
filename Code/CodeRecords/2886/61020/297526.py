N = int(input())

socks_in_bag = input().split()
socks_on_desk = set()

nums_of_socks = []

for sock in socks_in_bag:
    if sock in socks_on_desk:
        socks_on_desk.remove(sock)
    else:
        socks_on_desk.add(sock)

    nums_of_socks.append(len(socks_on_desk))

print(max(nums_of_socks))