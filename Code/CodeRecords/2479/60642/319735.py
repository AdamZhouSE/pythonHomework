times = int(input())
for i in range(times):
    str1 = input()
    str2 = input()
    chars = []
    chars2 = []
    for j in str1:
        if(chars.count(j)==0):
            chars.append(j)
    for j in str2:
        if(chars2.count(j)==0):
            chars2.append(j)
    for j in range(len(chars2)):
        if(chars.count(chars2[j])==0):
            chars.append(chars2[j])
        else:
            chars.remove(chars2[j])
    chars.sort()
    print("".join(i for i in chars))