num = int(input())
for i in range(0,num):
    stri = list(input())
    patt = list(input())
    for j in range(0,len(stri)):
        if stri[j] in patt:
            print(stri[j])
            break
        if j == len(stri)-1:
            print("$")