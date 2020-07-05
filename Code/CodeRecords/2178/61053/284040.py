def countMagic(charlst):
    strlst = []
    for i in range(len(charlst)):
        for j in range(i+1):
                if charlst[j:i+1] in strlst:
                    continue
                else:
                    strlst.append(charlst[j:i])
        print(len(strlst))

if __name__ == "__main__":
    total = int(input())
    strlst = []
    charlst = input().replace(" ","")
    countMagic(charlst)