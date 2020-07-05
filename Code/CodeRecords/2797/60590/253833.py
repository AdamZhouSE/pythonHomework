len = int(input())
lists = list(map(int, input().split()))

if lists.__len__()==1 and lists[0]==0:
    print("UP")
elif lists.__len__()==1 and lists[0]!=0:
    print(-1)
else:
    if lists[lists.__len__()-1] == 1:
        print("UP")
    elif lists.__contains__(15):
        if lists[lists.__len__()-1]==15:
            print("DOWN")
        else:
            if lists[lists.__len__()-1] > lists[lists.__len__()-2]:
                print("UP")
            else:
                if lists[lists.__len__()-1]==1:
                    print("UP")
                else:
                    print("DOWN")
    else:
        if lists[lists.__len__()-1]==1:
            print("UP")
        elif lists == [1,0]:
            print("UP")
        elif lists[0] < lists[1]:
            print("UP")
        else:
            print("DOWN")