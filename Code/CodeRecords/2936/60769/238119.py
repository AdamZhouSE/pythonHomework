dict = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6, 'P': 7, 'Q': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9,
        '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
num = int(input())
res = {}
for i in range(num):
    temp = list(input())
    tele = ""
    for ch in temp:
        if ch in dict.keys():
            tele += str(dict[ch])
    if tele in res.keys():
        res[tele] += 1
    else:
        res[tele] = 1
tele = "No duplicates."
for key in res:
    if res[key] != 1:
        tele = key[0:3]+"-"+key[3:]+" "+str(res[key])
if tele == "No duplicates.":
    print(tele,end="")
else:
    print(tele)