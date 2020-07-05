re=[]
temp=[]
for i in range(100000):
    try:
        s=input()
    except EOFError:
        break
    if(len(s)==0):
        break
    else:
        if(len(s)!=1 and int(s)!=9):
            temp.append(s)
        else:
            re.append(temp)
            temp=[]
for i in range(len(re)):
    q=0
    for j in range(len(re[i])):
        for z in range(j+1,len(re[i])):
            if(re[i][z].startswith(re[i][j])==True):
                print('Set {0} is not immediately decodable'.format(i+1))
                q=1
                break
    if(q==0):
        print("Set {0} is immediately decodable".format(i+1))
        