import re
s = list([n for n in re.findall(r"[a-z]", input())])
c = input()[0]
letters = sorted(list(set(s+[c])))
print(letters[0] if letters[-1] == c else letters[letters.index(c)+1])