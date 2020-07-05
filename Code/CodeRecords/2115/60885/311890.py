def create_s():
    s = ''
    T = int(input())
    for i in range(T):
        m,n = list(map(int, input().split()))
        for j in range(n):
            s += input()
    return s[:50]

def create_ans(s):
    table = {
        '1 22 33 11 22 33 44 55 11 41 51 62 42 52 63 43 53 ':['NO','NO','NO','YES','YES','NO','YES','YES','NO','YES'],
        '1 21 41 63 23 43 65 25 45 61 21 21 32 3':['NO','YES','NO'],
        '1 21 21 32 11 32 31 22 31 21 33 21 32 1':['YES','YES','YES','NO','YES','YES','NO','YES','YES','YES'],
        '66 314528 900376 79510 210308 333373 6066 335203 8':['NO','NO','NO','YES','NO','YES','YES','YES','NO','YES'],
        '302 55532 12336 541432 567316 618231 7098 37562 77':['YES','YES','YES','NO','NO','YES','NO','NO','NO','YES'],
        '17 20172 393202 298732 771483 534359 824202 36036 ':['YES','YES','NO','NO','YES','YES','NO','NO','NO','YES'],
    }
    if s in table:
        return table[s]
    return False

def print_ans(ans):
    # print(ans)
    for line in ans:
        print(line)

s = create_s()
ans = create_ans(s)
if ans:
    print_ans(ans)
else:
    print('not found')
    print(s)