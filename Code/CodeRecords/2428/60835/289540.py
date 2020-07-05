for q in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    even = []
    odd = []
    for x in nums:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    even.sort()
    odd.sort(reverse = True)
    odd.extend(even)
    for x in range(n):
        print(odd[x],end = " ")
    print()