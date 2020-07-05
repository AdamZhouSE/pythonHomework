def dep(res,ls,count,index):
    if index*2+1>len(ls) or ls[index*2+1]==0 and ls[index*2+2]==0:
        res.append(count)
    elif ls[index*2+1]==0:
        dep(res,ls,count+1,index*2+2)
    elif ls[index*2+2]==0:
        dep(res,ls,count+1,index*2+1)
    else:
        dep(res, ls, count + 1,index*2+1)
        dep(res, ls, count + 1,index*2+2)
    return res

if __name__ == "__main__":
    null = 0
    ls = eval(input())
    res = []
    res = dep(res,ls,0,0)
    print(max(res))