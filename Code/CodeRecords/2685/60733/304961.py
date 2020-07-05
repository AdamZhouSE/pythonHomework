for _ in range(int(input())):    
    n = int(input())
    num_9 = n // 9
    if n % 9 != 0:
        head = str(n - 9 * num_9)
    else:
        head = ""
    print(head + "9" * num_9 + "0" * n)