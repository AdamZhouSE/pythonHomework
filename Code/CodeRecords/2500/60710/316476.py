A = eval(input())
B = sorted(A)
res = []


def pancakeRev(k, lists):
    x = lists[0:k]
    x.reverse()
    x.extend(lists[k:])
    return x


for i in range(0, len(B)):
    last = B[len(B) - 1 - i]
    indexLast = A.index(last)
    A = pancakeRev(indexLast + 1, A)
    A = pancakeRev(len(B) - i, A)
    if indexLast != 0:
        res.append(indexLast + 1)
    if len(B) - i != 1:
        res.append(len(B) - i)

print(res)
