def lianxi(list):
    if len(list)==1:
        print(1)
        return 1
    else:
        count=0
        for i in range(0,len(list)):
            if ''.join(list[i:len(list)]) not in ''.join(list[0:len(list)-1]):
                count=count+1
        a=count+lianxi(list[0:len(list)-1])
        print(a)
        return a

if __name__ == "__main__":
    a=int(input())
    str=input().split(' ')
    lianxi(str)