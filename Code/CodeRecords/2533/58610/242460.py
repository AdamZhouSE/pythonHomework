a = list(map(int, input().replace('[', '').replace(']', '').split(',')))
print([ele for ele in a if ele % 2 == 0] + [ele for ele in a if ele % 2 == 1])