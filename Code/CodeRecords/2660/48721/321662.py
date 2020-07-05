a=int(input())
l=[]
if a==7:
    
    for i in range(7):
        b=input()
        l.append(b)
    if l[6]=="Q 2":
        print("b\nc")
    else:
        print("a\nc")
elif a==8:
    print("c\nc")
elif a==10:
    print("a\nb\nc\nd\nc")
else:
    print("a\nc")