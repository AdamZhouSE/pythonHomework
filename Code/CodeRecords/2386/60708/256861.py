N=int(input())
for i in range(0,N):
    l=int(input())
    temp=input().split(" ")
    X=int(input())
    list=[]
    for item in temp:
        list.append(int(item))
    if l<4:
        print(0)
    else:
        check=0
        for a in range(0,l-3):
            if(check==1):
                break
            for b in range(a+1,l-2):
                if (check==1):
                    break
                for c in range(b+1,l-1):
                    if (check==1):
                        break
                    for d in range(c+1,l):
                        if (check==1): break
                        if(list[a]+list[b]+list[c]+list[d]==X):
                            check=1
                            break

        print(check)

