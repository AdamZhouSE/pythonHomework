start = input()
end = input()
wlist = input()
wlist = wlist.replace("[", "")
wlist = wlist.replace("]", "")
wlist = wlist.split(",")
flag = True
for i in range(0, len(wlist)):
    if end[2:] == wlist[i][2:]:
        flag = False
if flag:
    print("[]")