a = eval(input())
print([ele for ele in a if ele % 2 == 0] + [ele for ele in a if ele % 2 == 1])