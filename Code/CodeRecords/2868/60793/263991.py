input()
ls = list(map(int, input().split()))
ls_odd = [x for x in ls if x % 2 != 0]
ls_even = [x for x in ls if x % 2 == 0]
print(min(len(ls_even), len(ls_odd)))