t=int(input())
for i in range(t):
    source=list(input())
    a=source.copy()
    for j in range(len(source)):
        if(source[j]=="6"):
            source[j]="9"
    a_num=""
    for j in a:
        a_num=a_num+j
    source_num=""
    for j in source:
        source_num=source_num+j
    print(int(source_num)-int(a_num))
