def RomanVal(ch):
    if ch == 'I':
        return 1
    if ch == 'V':
        return 5
    if ch == 'X':
        return 10
    if ch ==  'L':
        return 50
    if ch == 'C':
        return 100
    if ch == 'D':
        return 500
    if ch == 'M':
        return 1000

def Roman2Int(str):
    lst = []
    for ch in str:
        lst.append(RomanVal(ch))
    val = 0
    for i in range(len(lst)):
        if i != len(lst)-1:
            if lst[i] < lst[i+1]:
                val -= lst[i]
            else:
                val += lst[i]
        else:
            val += lst[i]
    return val

if __name__ == "__main__":
    str = input()
    print(Roman2Int(str))