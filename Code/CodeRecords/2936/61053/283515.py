def isdigit(ch):
    return ch >= '0' and ch <= '9'

def letter2int(ch):
    if ch <= 'O':
        return int((ord(ch)-ord('A'))/3) + 2
    elif ch >= 'P' and ch <='S':
        return 7
    elif ch >= 'T' and ch <= 'V':
        return 8
    else:
        return 9

def transform(tel):
    res = ""
    for ch in tel:
        if isdigit(ch):
            res = res + ch
        elif ch == '-':
            continue
        else:
            res = res + str(letter2int(ch))
    return res

def printTel(tel):
    output = tel[0:3] + "-" + tel[3::]
    print(output,end=" ")

if __name__ == "__main__":
    total = int(input())
    dict = {}
    for i in range(total):
        tel = input()
        tel = transform(tel)
        if tel in dict:
            dict[tel] += 1
        else:
            dict[tel] = 1
    sorted(dict)
    flag = False
    for tel in dict:
        if dict[tel] > 1:
            flag = True
            printTel(tel)
            print(dict[tel])
    if not flag:
        print("No duplicates.",end="")