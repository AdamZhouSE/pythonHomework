
string = input()
leng = len(string)
allpos = []
first_char = []
for start in range(0,leng):
    pos = string[start:leng]
    allpos.append(pos)
    first_char.append(start)

result_pos = [allpos[0]]
result_idx = [first_char[0]]
for i in range(1,leng):
    word = allpos[i]
    inserted = False
    for j in range(0,i):
        if word < result_pos[j]:
            result_pos.insert(j,word)
            result_idx.insert(j,i)
            inserted = True
            break
    if not inserted:
        result_pos.append(word)
        result_idx.append(i)
print(' '.join(str(x+1) for x in result_idx))
