class edge:
    def _init_(start,end,value):
        self.start=start
        self.end=end
        self.value=value

class disjoint_set:
    def _init_(li):
        self.all=li
    def union(index1,index2):
        self.all[index1]+=self.all[index2]
        self.all.pop(index2)
    def check(element):
        for i in self.all:
            if element is in i:
                return self.all.index(i)
        return -1
    def add(element):
        self.all.append(element)
        
line1=input()
dot=int(input.strip().split()[0])
edge=int(input.strip().split()[1])
