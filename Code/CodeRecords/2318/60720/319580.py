import java.util.HashMap;
import java.util.Scanner;
 
/**
 * @Author fgf
 * @create 2020/3/10 22:12
 * 找到二叉树中的最大搜索二叉之树
 */
class Node {
    public int value;
    public Node left;
    public Node right;
    public Node(int data){
        this.value = data;
    }
}
 
public class Main {
    private static Node bstNode = null;
    private static int max = Integer.MIN_VALUE;
    private static int pre = Integer.MIN_VALUE;
 
    public static void getMaxBST(Node root){
        if(root == null)
            return;
        pre = Integer.MIN_VALUE;
        if(isBST(root)){
            int nodesNum = getNodesNum(root);
            if(nodesNum > max){
                max = nodesNum;
                bstNode = root;
            }
        }
        getMaxBST(root.left);
        getMaxBST(root.right);
    }
    //获得二叉树节点个数
    public static int getNodesNum(Node root){
        if(root == null)
            return 0;
        return 1 + getNodesNum(root.left) + getNodesNum(root.right);
    }
    //判断是否是一颗搜索二叉树 中序遍历 左中右
    public static boolean isBST(Node root){
        if(root == null)
            return true;
        boolean flagLeft = isBST(root.left);
        if(pre >= root.value)
            return false;
        pre = root.value;
        if(flagLeft == false)
            return false;
        else
            return isBST(root.right);
    }
 
 
    public static void main(String[] args) {
/**
13 6
6 1 12
1 -1 3
12 10 13
-1 0 0
3 0 0
10 4 14
13 20 16
4 2 5
14 11 15
2 0 0
5 0 0
11 0 0
15 0 0
 */
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        Node root = new Node(scanner.nextInt());
        HashMap<Integer, Node> hashMap = new HashMap<>();
        hashMap.put(root.value, root);
        int[][] nodes = new int[count][3];
        for(int i=0; i<count; i++){
            for(int j=0; j<3; j++){
                int v = scanner.nextInt();
                if(v != 0)
                    hashMap.put(v, new Node(v));
                nodes[i][j] = v;
            }
        }
        for(int i=0; i<count; i++){
            int[] arr = nodes[i];
            Node fakeRoot = hashMap.get(arr[0]);
            if(arr[1] != 0)
                fakeRoot.left = hashMap.get(arr[1]);
            if(arr[2] != 0)
                fakeRoot.right = hashMap.get(arr[2]);
        }
        root = hashMap.get(root.value);
        getMaxBST(root);
        System.out.println(max);
//        System.out.println(bstNode.value);
//        System.out.println(isBST(root));
    }
}