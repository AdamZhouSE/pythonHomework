n=int(input())
for i in range(n):
    num=input()
    k=list(num)
    for j in range(len(k)):
        if k[j]=='6':
            k[j]='9'
            continue
        if k[j]=='9':
            k[j]='6'
    res="".join(k)
    print(int(res)-int(num))