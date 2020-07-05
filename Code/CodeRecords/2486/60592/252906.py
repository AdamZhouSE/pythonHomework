def printst(list):
    ls = list[1:len(list)]
    if not '[' in ls:
        return list
    i = 0
    stri = ""
    while not list[i].isdigit():
        stri+=list[i]
        i+=1
    num = int(list[i])
    return  stri+num*printst(list[i+2:len(list)-1])

if __name__ == "__main__":
    tests = int(input())
    for i in range(0,tests):
        ls = input()
        num = int(ls[0])
        ls = ls[2:len(ls)-1]
        print(printst(ls)*num)