

import java.util.Stack;
 
class Node{
    Node left;
    Node right;
    char val;
    public void Node(char value){
        this.val = value;
    }
}
 
public class Solutions{
    public void preOrderUnRecur(Node head){
        //非递归 前序遍历
        if(head == null) return;
        Stack<Ndoe> sk = new Stack<>();
        sk.push(head);
        while(!sk.isEmpty()){
            //先访问中间结点，再将**右左**节点入栈
            head=sk.pop();
            System.out.print(n.val + " ");
            if(head.right != null){
                sk.push(head.right);
            }
            if(head.left!=null){
                sk.push(head.left);
            }
        }
    }
 
    public void inOrderUnRecur(Node head){
        //非递归，中序遍历
        if(head == null) return;
        Stack<Ndoe> sk = new Stack<>();
        while(head != null && !sk.isEmpty()){
            //先入栈，再访问。先走到最左叶子，再往回返着中序遍历
                sk.push(head);
                head = head.left;
            }else{
                head = sk.pop();
                System.out.print(n.val + " ");
                head = head.right;
            }
        }
    }
 
    public void posOrderUnRecur1(Node head){
         //非递归，后序遍历，双栈法
        if(head == null) return;
        Stack<Ndoe> s1 = new Stack<>();
        Stack<Ndoe> s2 = new Stack<>();
        s1.push(head);
        //子树根先入s1，再出栈入s2，同时它的先左后右子树入s1
        //左右子树出s1入s2后，变成右在下，左在上，出s2后顺序变成 左-右-中
        while(!s1.isEmpty()){
            head = s1.pop();
            s2.push(head);
            if(head.left != null){
                s1.push(head.right);
            }
            if(head.right!=null){
                s1.push(head.right);
            }
        }
        //s2出栈即访问
        while(!s2.isEmpty()){
            System.out.print(s2.pop().val+" ");
        }
    }
    public void posOrderUnRecur2(Node head){
        //非递归，后序遍历，辅助标记
        if(head == null) return;
        Stack<Ndoe> sk = new Stack<>();
        Node tmp = null;//标记
        while(head != null || !sk.isEmpty()){
            //一直往左走
            while(head!=null){
                sk.push(head);
                head = head.left;
            }
            //如果当前结点没访问过，且右子树不空，否则访问右子树
            head = sk.peek();
            if(head != tmp && head.right!=null){
                head = head.right;
            }els{//否则出栈，访问，并标记
                sk.pop();
                System.out.print(head.val + " ");
                tmp = head;
                head = null;//访问指针置空，从而后续打印：左右中
            }
        }
    }
}