T = int(input())
for i in range(T):
    s = input()
    k = int(input())
    clen = mlen = 0
    record = []
    for i in s:
        if i not in record:
            if clen == k:
                mlen = max(mlen, len(record))
                while record[1:].count(record[0]) != 0:
                    del record[0]
                del record[0]
            else:
                clen += 1
        record.append(i)
    print(max(mlen, len(record)))