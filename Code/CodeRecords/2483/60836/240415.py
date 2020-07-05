n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list)//2:
    result=False
    position=0
    str1 = list(string_list[i])
    patt = list(string_list[i+1])

    for m in range(len(str1)):
        for j in range(len(patt)):
            if patt[j]==str1[m]:
                position=j
                result=True
                break
        if result:
            break

    if result:
        print(patt[position])
    else:
        print("$")

    i=i+1