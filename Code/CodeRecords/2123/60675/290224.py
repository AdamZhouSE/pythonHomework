def isPow(n: int) -> bool:
    cnt = 1
    while True :
        if cnt * cnt == n :
            return True
        elif cnt * cnt < n :
            cnt += 1
            continue
        else:
            return False

n = int(input())
print(isPow(n))