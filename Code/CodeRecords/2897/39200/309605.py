word = [x[1:-1] for x in input()[1:-1].split(",")]
wordbits = []
for x in word:
    bits = "0"*26
    for y in x:
        bit = ord(y) - ord("a")
        if bits[bit] == "0":
            bits = bits[0:bit] + "1" + bits[bit + 1::]
    wordbits.append(int(bits, 2))
maxlength = 0
for x in range(len(word)):
    for y in range(x, len(word)):
        if wordbits[x] & wordbits[y] == 0:
            length = len(word[x]) * len(word[y])
            if length > maxlength:
                maxlength = length
print(maxlength)
