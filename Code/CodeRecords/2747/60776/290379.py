def digui(qi,zhong,list1,list2,danci,index):
    if(qi!=zhong):
        for i in range(0, len(qishi)):
            temp1 = qi
            for j in range(index,len(danci)):
                temp = []
                temp.extend(list1)
                str=temp1[0:i]+danci[j][i]+temp1[i+1:len(temp1)]
                if(str==danci[j]):
                    temp.append(str)
                    digui(str,zhong,temp,list2,danci,j+1)
    else:
        list2.append(list1)




if __name__ == "__main__":
    qishi=input()
    zhongzhi=input()
    danci=input()
    danci=danci.replace("[\"","")
    danci=danci.replace("\"]","")
    danci=danci.split("\",\"")
    result=[]
    digui(qishi,zhongzhi,[qishi],result,danci,0)
    minlen=10000
    for i in range(0,len(result)):
        if len(result[i])<minlen:
            minlen=len(result[i])

    if result==[]:
        print([])
    else:
        print("[")
        newresult = []
        for i in range(0, len(result)):
            if len(result[i]) == minlen:
                newresult.append(result[i])
        for i in range(0, len(newresult) - 1):
            print("  [\"", end="")
            print("\",\"".join(newresult[i]), end="")
            print("\"],")
        print("  [\"", end="")
        print("\",\"".join(newresult[len(newresult) - 1]), end="")
        print("\"]")
        print("]")