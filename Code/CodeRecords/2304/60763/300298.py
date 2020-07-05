import java.util.Scanner;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int rootVal = Integer.parseInt(str[1]);
        TreeNode[] nodes = new TreeNode[n+1];
        for(int i=1; i<n+1; i++){
            nodes[i] = new TreeNode(i);
        }
        for(int i=0; i<n; i++){
            str = sc.nextLine().split(" ");
            int fa = Integer.parseInt(str[0]);
            int left = Integer.parseInt(str[1]);
            int right = Integer.parseInt(str[2]);
            nodes[fa].left = nodes[left];
            nodes[fa].right = nodes[right];
        }
        //
        //关键在于记录层数
        levelTraverse(nodes[rootVal]);
        zigzagTraverse(nodes[rootVal]);



    }
    public static void zigzagTraverse(TreeNode root){
        if(root==null)
            return;
        LinkedList<TreeNode> deque = new LinkedList<>();
        deque.add(root);
        //下一层节点的数量, 从第二层开始记录, 第二层就是根节点的下一层
        int num = 0;
        //当前层还有多少节点没处理, 从第一层开始记录, 第一层还剩1个根节点没有处理
        int countdown = 1;
        //记录层数
        int level = 1;
        // 表示奇数层和偶数层, 约定: true表示奇数层, false表示偶数层; 从奇数层开始
        boolean flag = true;
        while(!deque.isEmpty()){
            //奇数层, 从队列头弹出元素, 打印; 左孩子先进队尾, 右孩子后进队尾
            if(flag==true){
                System.out.print("Level "+level+" from left to right: ");
                while(countdown>0){
                    TreeNode cur = deque.poll();
                    System.out.print(cur.val+" ");
                    countdown--;
                    if(cur.left!=null){
                        deque.add(cur.left);
                        num++;
                    }
                    if(cur.right!=null){
                        deque.add(cur.right);
                        num++;
                    }
                }
                System.out.println();
                //update; 下面这四句可以写到if else 的外面
                countdown = num;
                num = 0;
                flag = false;
                level++;
            }
            //偶数层, 从队尾弹出元素, 打印; 右孩子先进队首, 左孩子后进队首
            else{
                System.out.print("Level "+level+" from right to left: ");
                while(countdown>0){
                    TreeNode cur = deque.pollLast();
                    System.out.print(cur.val+" ");
                    countdown--;
                    if(cur.right!=null){
                        deque.addFirst(cur.right);
                        num++;
                    }
                    if(cur.left!=null){
                        deque.addFirst(cur.left);
                        num++;
                    }
                }
                System.out.println();
                //update
                countdown = num;
                num = 0;
                flag = true;
                level++;
            }
        }
    }
    public static void levelTraverse(TreeNode root){
        if(root==null)
            return;
        LinkedList<TreeNode> queue = new LinkedList<>();
        int level = 1;
        //num是下一层节点的数量; countdown是当前层还有几个节点没处理
        int num = 0, countdown = 1;
        queue.add(root);
        while(!queue.isEmpty()){
            System.out.print("Level "+level+" : ");
            while(countdown>0){
                TreeNode cur = queue.poll();
                System.out.print(cur.val+" ");
                countdown--;
                if(cur.left!=null){
                    queue.add(cur.left);
                    num++;
                }
                if(cur.right!=null){
                    queue.add(cur.right);
                    num++;
                }
            }
            System.out.println();
            //update
            countdown = num;
            num = 0;
            level++;
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
————————————————
版权声明：本文为CSDN博主「littlehaes」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/littlehaes/article/details/103543597