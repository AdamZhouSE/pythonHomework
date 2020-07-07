import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
 
class TreeNode{
    public int val;
    public TreeNode right;
    public TreeNode left;
    public TreeNode parent;
    public TreeNode(int val){
        this.val = val;
    }
}
public class Main{
    private static TreeNode pre;
 
    public static void main(String[] args) throws IOException{
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(input.readLine());
        int[][] arr = new int[n+1][2];
        String[] str = input.readLine().split(" ");
        int root = Integer.parseInt(str[0]);
        arr[root][0] = Integer.parseInt(str[1]);
        arr[root][1] = Integer.parseInt(str[2]);
        int index = 0;
        for(int i=1;i<n;i++){
            String[] strings = input.readLine().split(" ");
            index = Integer.parseInt(strings[0]);
            arr[index][0] = Integer.parseInt(strings[1]);
            arr[index][1] = Integer.parseInt(strings[2]);
        }
        TreeNode treeNode = new TreeNode(root);
        createTree(treeNode,arr);
        TreeNode head = convert(treeNode);
        StringBuilder builder = new StringBuilder();
        TreeNode node = head;
        while(node!=null){
            builder.append(node.val).append(" ");
            node = node.right;
        }
        System.out.print(builder.toString());
 
    }
        public static void createTree(TreeNode root,int[][]a){
        if(root==null){
            return;
        }
        int i = root.val;
        int l = a[i][0];
        int r = a[i][1];
        if(l!=0){
            TreeNode leftNode = new TreeNode(l);
            root.left = leftNode;
            leftNode.parent = root;
            createTree(leftNode,a);
        }if(r!=0){
            TreeNode rightNode = new TreeNode(r);
            root.right = rightNode;
            rightNode.parent = root;
            createTree(rightNode,a);
        }
    }
 
    public static TreeNode convert(TreeNode head){
 
        Queue<TreeNode> queue = new LinkedList<>();
        inOrder(head,queue);
        if(queue.isEmpty()){
            return head;
        }
        head = queue.poll();
        TreeNode pre = head;
        pre.left = null;
        TreeNode cur = null;
        while(!queue.isEmpty()){
            cur = queue.poll();
            pre.right = cur;
            cur.left = pre;
            pre = cur;
        }
        return head;
    }
 
    public static void inOrder(TreeNode root, Queue<TreeNode> queue){
        if(root==null){
            return;
        }
        inOrder(root.left,queue);
        queue.add(root);
        inOrder(root.right,queue);
    }
}