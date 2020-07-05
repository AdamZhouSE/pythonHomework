import sys
class Binary_search_tree:
    def __init__(self,sequence):
        self.root=None
        self.left=None
        self.right=None
        for i in list(sequence):
            self.insert(i)
    def insert(self,node):
        if self.root is None:
            
while True:
    a=int(input().strip())
    if a==0:
        sys.exit(0)
    standard=Binary_search_tree(input().strip())
    for i in range(a):
        com=Binary_search_tree(input().strip())
        if is_equal(standard,com):
            print('YES')
        else:
            print('NO')
