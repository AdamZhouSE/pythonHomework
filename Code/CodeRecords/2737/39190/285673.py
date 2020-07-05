def func3(list):
    num=len(list)/3
    res=[]
    for i in list:
        if res.count(i)==0 and list.count(i)>num:
            res.append(i)
    print(res)

ip=input()
func3(eval(ip))