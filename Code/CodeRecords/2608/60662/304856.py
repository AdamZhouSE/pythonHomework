from itertools import combinations


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


n = int(input())
for i in range(0, n):
    s = list(input())
    start = 0
    end = len(s) - 1
    res = list()
    while start < end:
        if is_vowel(s[start]):
            temp = [s[start]]
            nextOne = start + 1
            while nextOne <= end:
                if is_vowel(s[nextOne]):
                    if nextOne != end:
                        temp.append(s[nextOne])
                else:
                    temp.append(s[nextOne])
                    res.append(''.join(temp))
                nextOne = nextOne + 1
        start = start + 1
    for item in res:
        if len(item) > 2:
            one = list(item)
            arr = list(item)
            res.append(''.join([arr[0],arr[len(arr)-1]]))
            del arr[0]
            del arr[len(arr) - 1]
            for k in range(1,len(arr)):
                now = list(combinations(arr,k))
                for f in now:
                    res.append(''.join([one[0],''.join(f),one[len(one)-1]]))
    result = []
    for d in res:
        if d not in result:
            result.append(d)
    if len(result)==0:
        print(-1)
    else:
        for f in range(0, len(sorted(result))-1):
            print(sorted(result)[f], end=" ")
        print(sorted(result)[len(sorted(result))-1])