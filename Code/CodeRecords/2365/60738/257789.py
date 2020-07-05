n=int(input())
for i in range(n):
    a=int(input())
    output=""
    num_list=list(map(int,input().split()))
    max_length=len(str(max(num_list)))
    for j in range(a):
        templist=[]
        length=len(str(num_list[j]))
        templist.append([num_list[j]*10**(max_length-length)+int(str(num_list[j][0]))*10**(max_length-length),length])
        templist.sort()
        for k in range(a):
            output+=str(templist[i][0])[0:length]
        print(output)
    