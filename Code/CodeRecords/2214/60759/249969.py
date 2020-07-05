lst1 = list(map(int, input()[:-1].split('+')))
lst2 = list(map(int, input()[:-1].split('+')))
ans = str(lst1[0] * lst2[0] - lst1[1] * lst2[1]) + '+' + str(lst1[0] * lst2[1] + lst1[1] * lst2[0]) + 'i'
print(ans)
