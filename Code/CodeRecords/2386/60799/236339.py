T = int(input())
for hhh in range(0, T):
    input()
    List = [int(i) for i in input().split()]
    List.sort()
    k = int(input())
    flag = 0
    for i in range(0, len(List)):
        for j in range(i + 1, len(List)):
            for k in range(j + 1, len(List)):
                for l in range(k + 1, len(List)):
                    if List[i] + List[j] + List[k] + List[l] == k:
                        flag = 1
    print(flag)