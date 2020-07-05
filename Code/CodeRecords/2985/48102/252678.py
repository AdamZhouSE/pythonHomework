def put(n: int) -> str:
    if n == 1:
        return 'A'
    else:
        return put(n-1) + chr(ord('A')+n-1) + put(n-1)


num = int(input())
print(put(num))