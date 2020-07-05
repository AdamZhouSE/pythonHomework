import re 
def exam2():
    x = re.split("\[|\]|,", input())
    x.remove(x[0])
    x.remove(x[len(x)-1])
    n=[]
    for item in x:
        n.append(int(item))
    n.sort()
    print(n)
exam2()