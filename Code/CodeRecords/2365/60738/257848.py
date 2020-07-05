n=int(input())
for i in range(n):
    a=int(input())
    output=""
    num_list=list(map(int,input().split()))
    max_length=len(str(max(num_list)))
    templist=[]
    length=0
    for j in range(a):
        length=len(str(num_list[j]))
        if length!=max_length:
            templist.append([num_list[j]*10**(max_length-length)+int(str(num_list[j])[0])*10**(max_length-length-1),length])
        else:
            templist.append([num_list[j],length])
    templist.sort()
    templist.reverse()
    for k in range(a):
        output+=str(templist[k][0])[0:templist[k][1]]
    print(output)
    