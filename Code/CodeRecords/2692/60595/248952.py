def Test():
    weights=eval(input())
    D=int(input())
    right=sum(weights)
    left=max(right//D,max(weights))
    while left<=right:
        m, need, cur = (left + right) // 2, 1, 0
        for w in weights:
            if cur + w > m:
                need += 1
                cur = 0
            cur += w
        if need > D:
            left = m + 1
        else:
            right = m - 1
        print(left)
if __name__ == "__main__":
    Test()