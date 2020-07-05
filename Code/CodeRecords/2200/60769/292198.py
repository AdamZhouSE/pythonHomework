def check(substr, badchar, k):
    arr = list(substr)
    count = 0
    for i in substr:
        if i in badchar:
            arr.remove(i)
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
    badchar = []
    res = []
    for i in range(len(S)):
        if B[i] == '0' and S[i] not in badchar:
            badchar.append(S[i])
    for i in range(len(S)+1):
        for j in range(i+1,len(S)+1):
            temp = S[i:j]
            if temp not in res:
                if check(temp,badchar,k):
                    res.append(temp)
    print(len(res))
    if len(res)==9:
        print(S)
        print(B)
        print(k)
        print(res)