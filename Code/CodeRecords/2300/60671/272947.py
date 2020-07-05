class node:
    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class tree:
    def __init__(self, root=node()):
        self.root = root
        
def inorder_probing(now_node, in_L):
    if now_node.lchild:
        inorder_probing(now_node.lchild, in_L)
    in_L.append(now_node.elem)
    if now_node.rchild:
        inorder_probing(now_node.rchild, in_L)

def tree_establish(pre_list, index):
    
    if (len(pre_list) == 0 || index == len(pre_list) || pre_list[index] == '#')
        return None
    BNode* T = new BNode(preOrder[index++]);
    T->left = constructBinaryTree(preOrder, index);
    T->right = constructBinaryTree(preOrder, ++index);
    return T;

        
if __name__ == "__main__" :
    in_list = []
    pre_list = input()
    
    tree=tree_establish(pre_list,0)
    
    inorder_probing(tree.root, in_list)
        
        