T=int(input())
for i in range(T):
    str=input()
    patt=input()
    for j in range(len(str)):
        if str[j] in patt:
            print(str[j])
            break
    else:
        print("$")