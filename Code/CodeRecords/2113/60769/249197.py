dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
        8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
        14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
        19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
        60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "Hundred",
        1000: "Thousand", 1000000: "Million", 1000000000: "Billion"}


def resolve(do):
    localres = ""
    if len(do) != 3:
        do = "0" * (3 - len(do)) + do
    if int(do[1:]) in dict.keys():
        localres = dict[int(do[1:])] + localres
    else:
        localres = dict[int(do[2])] + localres
        if "0" != do[1]:
            localres = dict[int(do[1]) * 10] + " " + localres
    if "0" != do[0]:
        localres = localres = dict[int(do[0])] + " Hundred " + localres
    return localres


num = input()
res = ""
if len(num) > 3:
    do = num[-3:]
    num = num[:-3]
    res = resolve(do) + " "+res
    res = dict[1000] + " " + res
if len(num) > 3:
    do = num[-3:]
    num = num[:-3]
    res = resolve(do) + " "+res
    res = dict[1000000] + " " + res
if len(num) > 3:
    do = num[-3:]
    num = num[:-3]
    res = resolve(do) + " "+res
    res = dict[1000000000] + " " + res

res = resolve(num) + " "+res
print(res.strip())
