def resort(nStr):
    res="false"
    for i in range(0,31):
        temp=sorted(str(2**i))
        if temp==sorted(nStr):
            res="true"
            return res
        elif len(temp)>len(nStr):
            return res
    return res

if __name__ == "__main__":
    n = input()
    nStr = str(n)
    res=resort(nStr)
    print(res)