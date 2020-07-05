def check(substr,  k):
    count = 0
    for i in substr:
        if i == '0':
            count += 1
        if count > k:
            # print("false")
            return False
        # print(arr)
    return True


if __name__ == '__main__':
    S = list(input())
    B = list(input())
    k = int(input())
    res = []
    for i in range(len(B) + 1):
        for j in range(i + 1, len(B) + 1):
            temp = B[i:j]
            if check(temp, k):
                if S[i:j] not in res:
                    res.append(S[i:j])
    print(len(res))
    # print(res)