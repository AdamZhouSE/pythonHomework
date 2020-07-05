ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Ninteen"]
huns = ["Hundred", "Thousand", "Million", "Billion"]

ans = []

def toInt(s):
    return ord(s) - ord('0')

def toWord(s):
    global ones, tens, teens, huns
    while len(s) < 3: s = "0" + s
    if s[0] != "0":
        ans.append(ones[toInt(s[0])])
        ans.append(huns[0])
    if s[1] == "1" and s[2] != "0":
        ans.append(teens[toInt(s[2])])
    else:
        if s[1] != "0":
            ans.append(tens[toInt(s[1])])
        if s[2] != "0":
            ans.append(ones[toInt(s[2])])

s = input()
n = len(s)
if n % 3 == 0: m = 3
else: m = n - n // 3 * 3

toWord(s[:m])
s = s[m:]
if len(s) > 0: ans.append(huns[len(s) // 3])

for i in range(m, n, 3):
    toWord(s[:3])
    s = s[3:]
    if len(s) > 0: ans.append(huns[len(s) // 3])

print(" ".join(ans))