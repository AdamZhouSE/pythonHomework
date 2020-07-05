def sort(string1,string2):
    value_eq='='
    for i in range(min(len(string2),len(string1))):
        if string2[i]>string1[i]:
            value_eq='<'
            break
        if string2[i]<string1[i]:
            value_eq='>'
            break
    if value_eq=='=':
        if len(string1) > len(string2):
            value_eq='>'
        if len(string1) < len(string2):
            value_eq='<'
    return value_eq

def operate(string3):
    a=[]
    for i in range(len(string3)):
        a.append(string3[i:len(string3)])
    b=[]
    for i in range(len(string3)):
        b.append(i+1)
    for i in range(len(string3)-1):
        for j in range(len(string3)-1-i):
            if sort(a[j],a[j+1])=='>':
                a[j],a[j+1]=a[j+1],a[j]
                b[j], b[j + 1] = b[j + 1], b[j]
    for i in range(len(b)-1):
        print(b[i],end=" ")
    print(b[-1])

operate(input())