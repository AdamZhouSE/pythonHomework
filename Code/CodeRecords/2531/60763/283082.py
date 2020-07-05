from collections import Counter
import collections

def SortString(T):
    count = collections.Counter(T)
    ans = [T[0]]
    count[T[0]] = 0
    print(count)
    for c in (1,len(T)):
        for i in ans:
            if count[i] <= count[T[c]]:
                for j in range(count[T[c]]):
                    ans.insert(0,T[c])
        print(ans)
        # Set count[c] = 0 to denote that we do not need
        # to write 'c' to our answer anymore.
        count[T[c]] = 0
        print(count)
    return "".join(ans)

def frequencySort( s: str) -> str:
    return ''.join(i * j for i, j in Counter(s).most_common())


t = ''+input()
print(frequencySort(t))