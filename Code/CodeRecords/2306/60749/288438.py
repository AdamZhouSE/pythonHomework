/*
Morris遍历
从root开始; 围绕当前节点的左孩子的最右节点的右指针展开
根据当前节点有没有左孩子分成两种情况讨论

while(cur!=null)
当前节点没有左孩子时
    cur = cur.right
当前节点有左孩子时
    找到cur左孩子的最右节点node
        如果node的右指针为null, 令node.right=cur, cur = cur.left
        如果node的右指针不为null, 令node.right=null, cur = cur.right
*/
import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int rootVal = Integer.parseInt(str[1]);
        TreeNode[] nodes = new TreeNode[n+1];
        //初始化各个节点
        for(int i=1; i<=n; i++){
            nodes[i] = new TreeNode(i);
        }
        for(int i=1;i<=n; i++){
            str = sc.nextLine().split(" ");
            int val = Integer.parseInt(str[0]);
            int left = Integer.parseInt(str[1]);
            int right = Integer.parseInt(str[2]);
            nodes[val].left = left==0?null:nodes[left];
            nodes[val].right = right==0?null:nodes[right];
        }
        TreeNode root = nodes[rootVal];
        morrisPre(root);
        morrisIn(root);
        morrisPos(root);
    }
    //前序
    public static void morrisPre(TreeNode root){
        if(root==null)
            return;
        TreeNode cur = root;
        while(cur!=null){
            if(cur.left==null){
                System.out.print(cur.val+" ");
                cur = cur.right;
            }
            else{
                TreeNode node = cur.left;
                //寻找cur左孩子的最右节点
                while(node.right!=null && node.right!=cur){
                    node = node.right;
                }
                //here, 要么node.right==null, 要么node.right==cur
                if(node.right==null){
                    System.out.print(cur.val+" ");
                    node.right = cur;
                    cur = cur.left;
                }
                else{
                    //恢复当前节点的右指针
                    node.right = null;
                    //执行完下面这句就会第二次访问cur
                    cur = cur.right;
                }
            }
        }
        System.out.println();
    }
    //中序
    public static void morrisIn(TreeNode root){
        if(root==null)
            return;
        TreeNode cur=root;
        while(cur!=null){
            if(cur.left==null){
                System.out.print(cur.val+" ");
                //这句执行后, 可能回到某个节点, 也可能指向null; 指向null说明cur是整棵树的最右节点
                cur = cur.right;
            }
            else{
                TreeNode node = cur.left;
                while(node.right!=null && node.right!=cur){
                    node = node.right;
                }
                if(node.right==null){
                    node.right=cur;
                    cur = cur.left;
                }
                else{
                    System.out.print(cur.val+" ");
                    //恢复右指针
                    node.right=null;
                    cur = cur.right;
                }
            }
        }
        System.out.println();
    }
    //后序; 核心:第二次访问某个节点时, 逆序打印该节点左子树的右边界
    //只打印访问两次的节点
    public static void morrisPos(TreeNode root){
        if(root==null)
            return;
        TreeNode cur = root;
        while(cur!=null){
            if(cur.left==null){
                cur = cur.right;
            }
            else{
                TreeNode node = cur.left;
                while(node.right!=null && node.right!=cur){
                    node = node.right;
                }
                if(node.right==null){
                    node.right = cur;
                    cur = cur.left;
                }
                else{
                    //核心:先把cur左子树最右节点的右指针恢复, 再逆序打印cur左子树右边界
                    node.right = null;
                    printRightEdge(cur.left);
                    cur = cur.right;
                }
            }
        }
        //最后再打印右边界
        printRightEdge(root);
    }
    public static void printRightEdge(TreeNode root){
        //反转单向链表
        TreeNode left=null, cur=root, right=null;
        while(cur!=null){
            //save next
            right = cur.right;
            //change direction
            cur.right = left;
            //update
            left = cur;
            cur = right;
        }
        
        //print and 恢复
        cur = left;
        while(cur != null){
            System.out.print(cur.val+" ");
            //save next
            left = cur.right;
            //change direction
            cur.right = right;
            //update
            right = cur;
            cur = left;
        }
    }
    public static class TreeNode{
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val){
            this.val = val;
        }
    }
}
