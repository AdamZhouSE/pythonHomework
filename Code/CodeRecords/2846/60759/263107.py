n = int(input())
lst = list(map(int, input().split(' ')))
set_p = set([i for i in lst if i > 0])
set_n = set([i for i in lst if i < 0])
print(len(set_p) + len(set_n))
