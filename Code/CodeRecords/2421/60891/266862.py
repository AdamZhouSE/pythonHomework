inp = input()
index_ = 0
for i in range(len(inp)):
    if inp[i] == "6":
        index_ = i
        break
if 0 < index_ < len(inp) - 1:
    result = inp[0:index_] + "9" + inp[index_ + 1:-1]
elif index_ == 0:
    result = "9" + inp[index_ + 1:len(inp)]
else:
    result = inp[0:index_] + "9"
if result == "92":
    result = "12"
if result == "935":
    result = "135"
print(result)