def find_min(n):
    global num
    if n==1:
        num += 1
        return
    if n%2==0:
        num += 1
        find_min(n//2)
    else:
        num += 2
        find_min(n//2)
    return

t = int(input())
for k in range(t):
    n = int(input())
    num = 0
    find_min(n)
    print(num)