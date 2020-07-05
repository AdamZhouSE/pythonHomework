def max_num_of_toys(cost_list, K):
    cost_list.sort()
    if (len(cost_list) == 1):
        if cost_list[0] <= K:
            return 1

        else:
            return 0

    if cost_list[0] > K:
        return 0

    return 1 + max_num_of_toys(cost_list[1:], K - cost_list[0])


T = int(input())
for i in range(T):
    N_and_K = input().split()
    cost_list = input().split()

    K = int(N_and_K[1])
    for j in range(len(cost_list)):
        cost_list[j] = int(cost_list[j])

    cost_list.sort()
    print(max_num_of_toys(cost_list, K))
