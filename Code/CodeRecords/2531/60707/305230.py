
from collections import Counter


def frequencySort(s: str) -> str:
    d = Counter(s)
    res = sorted(d, key = d.get, reverse=True)     
    return ''.join([x*d[x] for x in res])



if __name__ == '__main__':
    s = input()
    res = frequencySort(s)
    print(res)