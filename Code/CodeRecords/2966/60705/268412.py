def solve():
    [n, m] = list(map(int, input().split(" ")))
    S = input().replace(" ", "", n)
    T = input().replace(" ", "", n)
    for i in range(1, n-1):
        for j in range(i+1, n):
            if T[:i] + T[i:j] + T[j:] == S:
                print("YES")
                print("1 " + str(i))
                print(str(i+1) + " " + str(j))
                print(str(j+1) + " " + str(n))
                return
            elif T[:i] + T[j:]+T[i:j] == S:
                print("YES")
                print("1 " + str(i))
                print(str(j + 1) + " " + str(n))
                print(str(i + 1) + " " + str(j))
                return
            elif T[i:j] + T[j:] + T[:i] == S:
                print("YES")
                print(str(i + 1) + " " + str(j))
                print(str(j + 1) + " " + str(n))
                print("1 " + str(i))
                return
            elif T[i:j] + T[:i] + T[j:] == S:
                print("YES")
                print(str(i + 1) + " " + str(j))
                print("1 " + str(i))
                print(str(j + 1) + " " + str(n))
                return
            elif T[j:] + T[i:j] + T[:i] == S:
                if j == 4 and i == 1:
                    print(S)
                    print(T)
                print("YES")
                print(str(j + 1) + " " + str(n))
                print(str(i + 1) + " " + str(j))
                print("1 " + str(i))
                return
            elif T[j:] + T[:i] + T[i:j] == S:
                print("YES")
                print(str(j + 1) + " " + str(n))
                print("1 " + str(i))
                print(str(i + 1) + " " + str(j))
                return
            else:
                continue
    print("NO")
    return


if __name__ == '__main__':
    cases = int(input())
    for case in range(0, cases):
        solve()
