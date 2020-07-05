list=[1,1,2]

def digui(a):
    global list
    if a<len(list):
        return list[a]
    else :
        temp = 0
        for i in range(0, a):
            temp = temp + digui(i) * digui(a - i-1)
        list.append(temp)
        return list[a]

if __name__ == "__main__":
    a=int(input())
    for k in range(0,a):
        a=int(int(input())/2)
        print(digui(a))