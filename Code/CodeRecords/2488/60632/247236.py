data = eval(input())
supp = data.copy()
result = []
maxi = max(data)
mini = min(data)
for i in range(len(data)):
    if i % 2 == 0:
        result.append(mini)
        supp.remove(mini)
        mini = min(supp) if len(supp) != 0 else mini
    else:
        result.append(maxi)
        supp.remove(maxi)
        maxi = max(supp) if len(supp) != 0 else maxi
print(result)
