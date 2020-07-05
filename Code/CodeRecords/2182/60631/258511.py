def jo(n, m):
    if type(n) != type(1) or n <= 0:
        raise Exception('n must be an integer(n > 0)')
    if n == 1:
        return 0
    else:
        return (jo(n - 1, m) + m) % n
p=int(input())
for i in range(p):
    st = input()
    n = int(st.split(' ')[0])
    m = int(st.split(' ')[1])
    print(jo(n,m)+1)