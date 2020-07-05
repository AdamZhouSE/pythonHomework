def test(strings, count):
    flag = True
    for i in range(len(strings)):
        for j in range(i+1,len(strings)):
            if strings[j].startswith(strings[i]) or strings[i].startswith(strings[j]):
                flag = False
                break
    if flag:
        print('Set {} is immediately decodable'.format(count))
    else:
        print('Set {} is not immediately decodable'.format(count))


strings = []
count = 1
for line in iter(input,''):
    if line!='9':
        strings.append(line)
    else:  # line == '9'
        test(strings,count)
        strings = []
        count+=1