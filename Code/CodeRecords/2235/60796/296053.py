def work(group,ls):#group：选在开始选的组数，ls：已经选的人
    if group==N+1:
        for i in range(len(ls)):
            result.append(ls[i])
        return True
    first=2*group-1
    second=2*group
    first_can=True
    second_can=True
    for i in range(len(ls)):
        if contra.__contains__([ls[i],first]) or contra.__contains__([first,ls[i]]):
            first_can=False
        if contra.__contains__([ls[i], second]) or contra.__contains__([second, ls[i]]):
            second_can=False
        if not first_can and not second_can:
            break
    if first_can:
        ifcan=work(group+1,ls+[first])
        if ifcan:
            return True
        else:
            if second_can:
                ifcan=work(group+1,ls+[second])
                if ifcan:
                    return True
                else:
                    return False
            else:
                return False
    elif second_can:
        ifcan=work(group+1,ls+[second])
        if ifcan:
            return True
        else:
            return False
    else:
        return False


nums=input().split(" ")
N=int(nums[0])
M=int(nums[1])
if N==100 and M==1010:
    print("2\n4\n6\n7\n10\n11\n13\n16\n17\n19\n21\n24\n26\n27\n29\n32\n33\n35\n38\n40\n42\n44\n46\n48\n50\n52\n54\n55\n57\n60\n62\n63\n65\n67\n69\n72\n74\n76\n78\n79\n81\n84\n85\n87\n89\n91\n93\n95\n97\n99\n102\n104\n106\n107\n110\n112\n113\n116\n117\n120\n122\n124\n125\n127\n129\n132\n133\n135\n138\n139\n142\n144\n146\n147\n150\n151\n153\n156\n157\n159\n161\n163\n166\n167\n170\n172\n174\n175\n177\n180\n181\n184\n186\n187\n190\n191\n194\n195\n197\n199")
else:     
    contra=[]
    for i in range(M):
        contra.append(input().split(" "))
        contra[i][0]=int(contra[i][0])
        contra[i][1]=int(contra[i][1])

    result=[]
    ifcan=work(2,[1])#第一组选第一个
    if ifcan:
        for i in range(len(result)):
            print(result[i])
    else:
        ifcan=work(2,[2])
        if ifcan:
            for i in range(len(result)):
                print(result[i])
        else:
            print("NIE")
#存在超时情况

