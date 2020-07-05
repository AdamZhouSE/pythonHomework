T = int(input())
for hhh in range(0, T):
    input()
    List = [int(i) for i in input().split()]
    X = int(input())
    flag = 0
    for i in range(0, len(List) - 3):
        for j in range(i + 1, len(List) - 2):
            for k in range(j + 1, len(List) - 1):
                for l in range(k + 1, len(List)):
                    aaa = List[i] + List[j] + List[k] + List[l] == X
                    if aaa:
                        flag = 1
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    print(flag)