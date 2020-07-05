A = input().replace("[", "").replace("]", "").split(",")
result = []
for each in A:
    each = int(each)
    if each % 2 == 0:
        result.insert(0, each)
    else:
        result.append(each)
print(result)
