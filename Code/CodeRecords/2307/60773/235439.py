num=int(input());
get=[]
get.append(str(num))

for i in range(num*2):
    #print(i)
    s = input()
    get.append(s.replace(" ",""))


for i in range(1,num*2,2):
    n=int(get[i])
    #print(n)
    list=[]
    #print(list)
    for j in range(len(get[i+1])):
        sum=1
        for k in range(j+1,len(get[i+1]),1):
            if(get[i+1][j]==get[i+1][k]):
                sum = sum+1
        #print("sum",end="")
        #print(sum)
        #print(list)
        if sum>(n/2):
            list.append(get[i+1][j])
    #print("list",end="")
    #print(list)
    for l in range(len(list)):
        for m in range(l+1,len(list),1):
            if list[m]==list[l]:
                list[m]=='#'
    #print(len(list))
    #print(-1)
    if (len(list) == 0):
        print(-1)
    for l in list:
        if l != '#':
            if l == list[len(list) - 1]:
                print(l)
            else:
                print(l, end="")