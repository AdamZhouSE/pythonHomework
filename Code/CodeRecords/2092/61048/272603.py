
class point(object):
    class Struct(object):
        def __init__(self,name,son):
            self.name=name
            self.son=son
    def make_struct(self,name,son):
        return self.Struct(name,son)

def numop14():
    num=int(input())
    students=[int(x) for x in input().split()]
    lst=[]
    p=point()
    for i in range(len(students)):
        lst.append(p.make_struct(i+1,students[i]))
    res=len(lst)

    for i in range(len(lst)):
        lenth=2
        nextpoint=lst[lst[i].son-1]
        while(lst[i].name!=nextpoint.son and lenth<=len(lst)):
            nextpoint=lst[nextpoint.son-1]
            lenth+=1
        if(lenth<res):
            res=lenth
    print(res,end='')
    return


numop14()