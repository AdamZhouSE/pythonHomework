def find_2_num(n):
    if n==1:
        return 2
    if n==2:
        return 3
    return find_2_num(n-2)+find_2_num(n-1)

n=int(input())
for i in range(n):
    m=int(input())
    print(find_2_num(m))