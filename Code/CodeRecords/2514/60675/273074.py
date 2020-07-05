def func(a : str, b : str) -> bool :
    try :
        sub = a
        mai = b
        for i in range(len(a) - 1):
            one = mai.index(a[i])
            sec = mai.index(a[i + 1])
            if one > sec:
                return False
            mai = mai[0:one] + mai[one + 1:len(mai)]
        return True
    except:
        return False

str = input().replace(" ","")
string = input().replace(" ","")
print(func(str,string))