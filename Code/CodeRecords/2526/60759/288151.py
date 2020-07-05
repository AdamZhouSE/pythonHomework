from re import findall


ans = []
ans.extend(map(int, findall('[-]*\d+', input())))
ans.extend(map(int, findall('[-]*\d+', input())))
print(sorted(ans))
