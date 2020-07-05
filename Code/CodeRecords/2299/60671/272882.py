class node:
    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class tree:
    def __init__(self, root=node()):
        self.root = root
        
def bi_search_tree_establish(List): 
    if List:
        mytree = tree(node(List[0]))
        for i in range(1, len(List)):
            temp_node = mytree.root
            while temp_node:
                if List[i] < temp_node.elem:
                    if temp_node.lchild:
                        temp_node = temp_node.lchild
                    else:
                        temp_node.lchild = node(List[i])
                        break
                else:
                    if temp_node.rchild:
                        temp_node = temp_node.rchild
                    else:
                        temp_node.rchild = node(List[i])
                        break
        return mytree
    else:
        return None


def preorder_probing(now_node, pre_L):
    pre_L.append(now_node.elem)
    if now_node.lchild:
        preorder_probing(now_node.lchild, pre_L)
    if now_node.rchild:
        preorder_probing(now_node.rchild, pre_L)


def cmp(a, b): 
    leng = len(a)
    if leng == len(b):
        for i in range(0, leng):
            if a[i] != b[i]:
                return -1
        return 0
    else:
        return -1


if __name__ == "__main__":

    N = int(input())
    S_List = [int(i) for i in input()]
    S_Tree = bi_search_tree_establish(S_List) 

    if S_Tree:
        S_pre_list = []
        preorder_probing(S_Tree.root, S_pre_list)

        for i in range(0, N):
            List = [int(i) for i in input()] 
            MyTree = bi_search_tree_establish(List)
            if MyTree:
                pre_list = []
                preorder_probing(MyTree.root, pre_list)

                if cmp(S_pre_list, pre_list) == 0:
                    print("YES")
                else:
                    print("NO")