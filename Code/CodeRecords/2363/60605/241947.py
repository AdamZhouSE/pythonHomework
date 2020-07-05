n = int(input())
bina = bin(n)[2:]
rev = ""
for i in list(bina):
    if i == "1": rev = rev + "0"
    if i == "0": rev = rev + "1"

print(int(rev, base=2))