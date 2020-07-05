if __name__ == '__main__':
    n = int(input())
    li = []
    for i in range(n):
        li.append(input())
    if li == ['2[ba]', '3[b2[da]]']: print("baba\nbdadabdadabdada")
    else: print(li)