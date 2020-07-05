def func3(list):
    num=len(list)/3
    res=[]
    for i in list:
        if list.count(i)>num:
            if res.count(i)==0:
                res.append(i)
    print(res)

ip=input()
func3(eval(ip))