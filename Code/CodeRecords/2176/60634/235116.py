string = input()

def compare(a,b):
    i = 0
    while i <= min(len(a),len(b)):
        if i == min(len(a),len(b)):
            return len(a) >= len(b)
        if a[i] < b[i]:
            return False
        if a[i] > b[i]:
            return True
        i += 1


source = []
i=0
while i < len(string):
    source.append(string[i:len(string)])
    i += 1

result = []
i = 0
for ch in source:
    judge = False
    j = 0
    for k in result:
        if compare(source[k],ch):
            result.insert(j, i)
            judge = True
            break
        j += 1
    if not judge:
        result.append(i)
    i += 1

out = ""
i = 0
while i < len(source):
    out = out + str(result[i]+1)
    if i != len(source)-1:
        out += " "
    i += 1

print(out)

