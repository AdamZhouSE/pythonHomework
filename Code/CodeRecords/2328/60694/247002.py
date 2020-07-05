li = sorted(map(int, input().split(",")))
if li[0] > 2:
    print("")
    exit()
elif li[-1] == 2:
    tmp = sorted(map(str, li), reverse=True).insert(2, ":")
    print("".join(tmp))
    exit()
else:
    ans = ""
    i = 0
    for i in range(len(li)):
        if li[i] > 2:
            break

    if li[i-1] == 2:
        ans = str(li[i-1])
        del li[i-1]
        for j in range(len(li)):
            if li[j] >= 4:
                break
        ans = ans + str(li[j-1])
        del li[j-1]
        if li[0] >= 6:
            print("")
            exit()
        if li[-1] >= 6:
            ans = ans + ":" + "".join(list(map(str, li)))
        else:
            ans = ans + ":" + "".join(list(map(str, reversed(li))))
    else:
        ans = str(li[i-1])
        del li[i-1]
        ans = ans + str(li[-1])
        del li[-1]
        if li[0] >= 6:
            print("")
            exit()
        if li[-1] >= 6:
            ans = ans + ":" + "".join(list(map(str, li)))
        else:
            ans = ans + ":" + "".join(list(map(str, reversed(li))))
print(ans)
