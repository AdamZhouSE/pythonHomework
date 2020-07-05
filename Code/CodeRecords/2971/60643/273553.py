if __name__=="__main__":
    inp=input()
    length=len(inp)
    suffix=[]
    for i in range(0,len(inp)):
        slice=inp[i:]
        suffix.append(slice)
    suffix=sorted(suffix)
    res=""
    for i in suffix:
        res=res+str(length-len(i)+1)+" "
    print(res,end="")