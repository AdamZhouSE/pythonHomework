def isBST(li: [int]) -> bool:
    leng = len(li)
    for i in range(leng):
        # l: 2i+1, r: 2i+2
        l = 2 * i + 1
        r = 2 * i + 2
        if l < leng and li[l] is not None:
            if li[l] > li[i]:
                return False
        if r < leng and li[r] is not None:
            if li[r] < li[i]:
                return False
    return True


if __name__ == '__main__':
    li = []
    x = input().strip()
    x = x[1:len(x)-1].split(",")
    for i in x:
        if i != "null":
            li.append(int(i))
        else:
            li.append(None)

    print(str(isBST(li)).lower())

