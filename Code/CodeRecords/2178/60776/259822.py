def lianxi(str):
    if len(str)==1:
        print(1)
        return 1
    else:
        count=0
        for i in range(0,len(str)):
            if str[i:len(str)] not in str[0:len(str)-1]:
                count=count+1
        a=count+lianxi(str[0:len(str)-1])
        print(a)
        return a

if __name__ == "__main__":
    a=int(input())
    str=input()
    lianxi(str)