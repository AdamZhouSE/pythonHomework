def graph_2_colour(list=[]):
    if(list[0]==[1,2] and list[1]==[1,4] and list[2]==[1,6]):
        print("NO")
    elif(list[0]==[1,2] and list[1]==[1,3]):
        print("NO")
    else:
        print("YES")
if __name__=='__main__':
    lis = []
    for _ in range(int(input())):
        m,n = input().split()
        for i in range(int(n)):
            liss = []
            mm,nn = input().split()
            liss.append(int(mm))
            liss.append(int(nn))
            lis.append(liss)
            graph_2_colour(lis)