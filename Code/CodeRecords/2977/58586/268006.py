def complement(src):
    res=""
    for c in src:
        if c.isalpha():
            if c.isupper():
                res+=chr(90-(ord(c)-ord("A")))
            else:
                res+=chr(122-(ord(c)-ord("a")))
        else:
            res+=c
    return res

while True:
    line=input()
    if line.strip()=="!":
        break
    print(complement(line))


