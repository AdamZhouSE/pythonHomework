#13
b = input()
t = input()
# bins = [b]
# triples = [t] #本来写的一定有一位错，就不包括在内了
bins = []
triples = []
bvalue = []
tvalue = []
for i in range(0,len(b)):
    temp = list(b)
    if b[i] == "0":
        temp[i] = "1"
    else:
        temp[i] = "0"
    bins.append("".join(temp))
for i in range(0,len(t)):
    temp = list(t)
    if t[i] == "0":
        temp[i] = "1"
        triples.append("".join(temp))
        temp[i] = "2"
        triples.append("".join(temp))
    if t[i] == "1":
        temp[i] = "0"
        triples.append("".join(temp))
        temp[i] = "2"
        triples.append("".join(temp))
    if t[i] == "2":
        temp[i] = "0"
        triples.append("".join(temp))
        temp[i] = "1"
        triples.append("".join(temp))

for item in bins:
    bvalue.append(int(item,2))
for item in triples:
    tvalue.append(int(item,3))

# print(bins)
# print(triples)
# print(bvalue)
# print(tvalue)

outcome = 0

for item in bvalue:
    if item in tvalue:
        outcome = item
        break


print(outcome,end="")

