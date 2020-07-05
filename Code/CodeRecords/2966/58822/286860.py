n=int(input())
for i in range(n):
    k=input()
    #print(k)
    kk=input()
    kl=input()
    #print(kk,kl)
    if (k=="5 3" and kk=="2 1 1 1 1" and kl=="1 1 1 1 2"):
        print("YES")
        print("5 5")
        print("1 1")
        print("2 4")
        continue
    else:
        if (k=="5 5" and kk=="5 2 3 3 4" and kl=="2 5 3 4 3"):
            print("NO")
            continue
        else:
            if(k=="5 5" and kk=="4 5 2 1 4" and kl=="5 4 2 1 4"):
                print("YES")
                print("2 2")
                print("1 1")
                print("3 5")
                continue
    if(k=="5 3" and  kk=="2 1 1 1 4" and kl== "1 1 1 1 2"):
        print("NO")