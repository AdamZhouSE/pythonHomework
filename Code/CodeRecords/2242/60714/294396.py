first = [int(x) for x in input().split(",")]
second = [int(x) for x in input().split(",")]
if first[0] < second[0] < first[2] and first[1] < second[1] < first[3] or \
        first[0] < second[0] <= first[2] and first[1] < second[3] < first[3] or \
        first[0] < second[2] < first[2] and first[1] < second[1] < first[3] or \
        first[0] < second[2] < first[2] and first[1] < second[3] < first[3]:
    print(True)
else:
    print(False)
