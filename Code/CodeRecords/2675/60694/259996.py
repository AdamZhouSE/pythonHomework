T = int(input())
for _ in range(T):
    N = input()
    maxi = ""
    for ch in N:
        if ch == "6":
            maxi += "9"
        else:
            maxi += ch
    ans = int(maxi) - int(N)
    print(ans)

