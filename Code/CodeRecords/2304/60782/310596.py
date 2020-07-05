import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
/**
 * Created by lxw, liwei4939@126.com on 2017/10/28.
 * 二叉树的按层打印，使用一个队列 两个变量
 * 二叉树的ZigZag打印，使用一个双端队列 LinkedList
 */
public class BinaryTree {
    
    public class Node{
        public int value;
        public Node left;
        public Node right;
 
        public Node(int data){
            this.value = data;
        }
    }
    
    public void printByLevel(Node head){
        if(head == null)
            return;
        Queue<Node> queue = new LinkedList<Node>();
        int level = 1;
        Node last = head;
        Node nlast = null;
        queue.offer(head);
        System.out.print("Level" + (level++) + ":");
        while (!queue.isEmpty()){
            head = queue.poll();
            System.out.print(head.value + " ");
            if(head.left != null){
                queue.offer(head.left);
                nlast = head.left;
            }
            if(head.right != null){
                queue.offer(head.right);
                nlast = head.right;
            }
            if(head == last && !queue.isEmpty()){
                System.out.print("\nLevel" + (level++) + ":");
                last = nlast;
            }
        }
        System.out.println();
    }
    
    public void printByZigZag(Node head){
        if(head == null)
            return;
        Deque<Node> dq = new LinkedList<Node>();
        int level =1;
        boolean lr = true;
        Node last = head;
        Node nlast = null;
        dq.offerFirst(head);
        printLevelAndOrientation(level++, lr);
        while (!dq.isEmpty()){
            if(lr){
                head = dq.pollFirst();
                if(head.left != null){
                    nlast = nlast==null ? head.left : nlast;
                    dq.offerLast(head.left);
                }
                if(head.right != null){
                    nlast = nlast==null ? head.right : nlast;
                    dq.offerLast(head.right);
                }
            } else {
                head = dq.pollLast();
                if(head.right != null){
                    nlast = nlast==null ? head.right : nlast;
                    dq.offerFirst(head.right);
                }
                if(head.left != null){
                    nlast = nlast==null ? head.left : nlast;
                    dq.offerFirst(head.left);
                }
            }
            System.out.print(head.value + " ");
            if(head == last && !dq.isEmpty()){
                lr = !lr;
                last = nlast;
                nlast =null;
                System.out.println();
                printLevelAndOrientation(level++, lr);
            }
        }
        System.out.println();
    }
    
    public void printLevelAndOrientation(int level, boolean lr){
        System.out.print("Level" + level + "from");
        System.out.print(lr ? "left to right": "right to left");
    }
}

