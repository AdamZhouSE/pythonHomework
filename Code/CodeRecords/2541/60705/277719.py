def wuxianxiu(relation, n):
    for item in relation:
        if n == item[0]:
            return False
    return True


n = int(input())
relation = []
_ = input()[2:-2].split("],[")
for item in _:
    relation.append(list(map(int, item.split(","))))
print(relation)
rest = [i for i in range(0, n)]

    