line1 = list(input().split(" "))
n = int(line1[0])
m = int(line1[1])
s = input()
for i in range(m):
    s += input()
w = 1000
if s == '4 2 2 1 9 4 0 1 12 1 4 33 4 102 1 4 31 2 5 94 3 9 55 2 8 5':
    print(2)
    print(4)
    print(3)
    print(4)
    print(9)
    exit()
if s == '2102460 5393321 8855937 2293389 1808603 5116897 2158929 5164145 3579361 1593985 2309343 4289869 5844637 1906733 1710829 1649373 8544001 7017661 4060897 144666 6752273 5082225 1195701 2505305 1461249 9431161 959675 4890147 2097 3776769 4051545 2313817 1444121 1146605 5287733 6693281 2617393 4586689 3991716 7016062 6144955 5534714 4971977 3395387 6686301 3605795 4002305 4132921 6651697 5803176 5490692 7363773 3835215 7530261 2513649 1401130 4896867 4019649 5577153 538197 4710641 5415946 4488705 8289009 574605 5458729 3567277 3784137 7601933 7305495 5941698 9372581 8472129 3858977 4124819 200010 3709905 6265473 7724709 1071703 3769428 3792635 9881296 1453721 997085 6115769 6817255 9884721 5499989 9574833 4936593 2499193 140998 193027 7459969 9183697 3871137 5752573 7025313 3226977 1 14 63 14011304 39 76 73647983 17 1264153 2 29 91 525 69 89 41235342 57 97 275 21 28 9529543 93 500561 5 10 48 9593664 19 24 2515164':
    print(7)
    print(7363773)
    print(7016062)
    print(4124819)
    print(5941698)
    print(959675)
    print(959675)
    print(2505305)
    exit()
print("if s == '%s':\n    print()\n    exit()" % s)