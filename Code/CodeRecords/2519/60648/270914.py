ls=sorted(eval(input()))
ls.reverse()
for i in range(len(ls)-2):
    if ls[i]<ls[i+1]+ls[i+2]:
        print(ls[i]+ls[i+1]+ls[i+2])
        break