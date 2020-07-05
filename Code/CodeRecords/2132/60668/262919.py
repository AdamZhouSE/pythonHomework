def nums_20_Nums(Str):
    co = []
    coun = 0
    listN = ["one","two","three","four","five","six","seven","eight","nine"]
    for item in listN:
        for i in range(len(item)):
            for j in range(len(Str)):
                if Str[j]==item[i]:
                    coun += 1
                    break
        if coun == len(item):
                co.append(listN.index(item)+1)
        coun = 0
    co = sorted(co)
    for ite in co:
        re = "".join(str(ite))
    print(re)
if __name__=='__main__':
    Str = input()
    nums_20_Nums(Str)