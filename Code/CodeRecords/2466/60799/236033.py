T = int(input())
for hhh in range(0, T):
    input()
    List = sorted([int(i) for i in input().split()])
    print(len([(i, j, k) for i in range(0, len(List) - 2) for j in range(i + 1, len(List) - 1) for k in range(j + 1, len(List)) if List[i] + List[j] > List[k]]))