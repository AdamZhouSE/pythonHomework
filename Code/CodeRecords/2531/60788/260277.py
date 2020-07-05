class Chara:
    def __init__(self,value,count):
        self.value=value
        self.count=count
        
        
def f(s):
    m=[]
    for i in list(s):
        m.append(Chara(i,list(s).count(i)))
    m.sort(key=lambda x:x.count,reverse=True)
    return ''.join([x.value for x in m])


print(f(input().strip()))