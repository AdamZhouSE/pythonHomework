list=[1,2]

def digui(a):
    global list
    if a<=len(list):
        return list[a-1]
    elif a==len(list)+1:
        list.append(list[i-1]+list[i-2])
        return list[a-1]
    else:
        return digui(a-1)+digui(a-2)

if __name__ == "__main__":
    a=int(input())
    for i in range(0,a):
        a=int(input())
        print(digui(a))
            