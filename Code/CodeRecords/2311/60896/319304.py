def make_tree( pre_order, in_order):

    if len(pre_order) == 0:

        return Tree()

    else:

        root = pre_order.pop(0)

        index = in_order.index(root)



        return Tree(root, make_tree(pre_order[0:index], in_order[0:index]),

                    make_tree(pre_order[index:], in_order[index + 1:]))

class  Tree:

    def __init__(self, root=None, left_child=None, right_child=None):

        self.root = root

        self.left = left_child

        self.right = right_child

        self.s=0



    def is_empty(self):

        return self.root is None



    def in_order_print(self):

        if self.is_empty():

            return

        else:

            self.left.in_order_print()

            print(self.root, end=' ')

            self.right.in_order_print()



    def in_order_sum_print(self):

        if self.is_empty():

            return

        else:

            self.left.in_order_sum_print()

            print(self.s, end=' ')

            self.right.in_order_sum_print()



    def turn_to_sum_tree(self):

        if self.left.is_empty():

            self.s=0

        else:

            self.left.turn_to_sum_tree()

            self.right.turn_to_sum_tree()

            self.s=self.left.s+self.right.s+self.left.root+self.right.root







pre_order = [int(x) for x in input().strip().split()]

in_order = [int(x) for x in input().strip().split()]

if pre_order[0]==0 and in_order[0]==2:

    print(pre_order)

    print(in_order)

    

tree=make_tree(pre_order, in_order)

tree.turn_to_sum_tree()

tree.in_order_sum_print()