s = input()
suc = [{"s": s[i:], "k": i + 1} for i in range(len(s) - 1, -1, -1)]
suc.sort(key=lambda x: x["s"])
print([x["k"] for x in suc])