class Path:
    def __init__(self,paths,values):
        self.paths=paths
        self.values=values
    def cal_value():
        t=0
        for i in values:
            t+=i
        return t
class Tree:
    def __init__(self, root=None, left_child=None, right_child=None,value=None):
        self.root = root
        self.left = left_child
        self.right = right_child
        self.value=value

    def is_empty(self):
        return self.root is None