cnt=input()
cnt=list(map(int,cnt.split(' ')))
cnt.sort()
if (cnt[2]==cnt[3] and cnt[2]==cnt[4] and cnt[2]==cnt[5]) :
    if(cnt[0]<cnt[1]):
        print("Bear")
    else:
        print("Elephant")
elif (cnt[2] == cnt[3] and cnt[2] == cnt[0] and cnt[2] == cnt[1]) :
    if (cnt[4] < cnt[5]):
        print("Bear")
    else:
        print("Elephant")
elif (cnt[2] == cnt[1] and cnt[2] == cnt[3] and cnt[2] == cnt[4]) :
    if (cnt[0] != cnt[5]):
        print("Bear")
    else:
        print("Elephant")

else:
    print("Alien")
