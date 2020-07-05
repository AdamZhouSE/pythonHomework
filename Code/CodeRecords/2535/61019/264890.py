if __name__ == '__main__':
    arr = eval(input())
    ans, big = 0, 0
    for k, v in enumerate(arr):
        big = max(big, v)
        ans += (1 if big == k else 0)
    print(ans)
