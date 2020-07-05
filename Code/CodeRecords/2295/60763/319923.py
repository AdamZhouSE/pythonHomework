import java.util.*;
public class Main {
    static HashMap<Integer, Integer[]> hm;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] str = sc.nextLine().split(" ");
        int n = Integer.parseInt(str[0]);
        int r = Integer.parseInt(str[1]);

        Integer[] child;
        hm = new HashMap<>();
        for(int i = 0;i < n;i++){
            String[] str1 = sc.nextLine().split(" ");
            int fa = Integer.parseInt(str1[0]);
            int lc = Integer.parseInt(str1[1]);
            int rc = Integer.parseInt(str1[2]);
            child = new Integer[2];
            child[0] = lc;
            child[1] = rc;
            hm.put(fa, child);
        }


        String[] str2 = sc.nextLine().split(" ");
        int o1 = Integer.parseInt(str2[0]);
        int o2 = Integer.parseInt(str2[1]);

        Node root = new Node(r);
        Node node1 = new Node(o1);
        Node node2 = new Node(o2);
        buildTree(root);
        Node res = LCA(root, node1, node2);
        System.out.println(res.val);
    }

    // 递归查找最近公共祖先
    private static Node LCA(Node root, Node node1, Node node2){
        if(root == null){
            return null;
        }
        if(root.val == node1.val){
            return node1;
        }
        if(root.val == node2.val){
            return node2;
        }
        Node left = LCA(root.left, node1,node2);
        Node right = LCA(root.right, node1,node2);
        if(left != null && right != null){
            return root;
        }else if(left == null){
            return right;
        }else{
            return left;
        }
    }

    private static void buildTree(Node root) {

        if (root == null) {
            return;
        }
        if(hm.containsKey(root.val)) {
            Node lc = null;
            Node rc =null;
            Integer[] ch = hm.get(root.val);
            if(ch[0]!= 0){
                lc = new Node(ch[0]);
                lc.parent = root;
            }
            if(ch[1]!= 0) {
                rc = new Node(ch[1]);
                rc.parent = root;
            }
            root.left = lc;
            root.right = rc;

            buildTree(lc);
            buildTree(rc);
        }
    }
}



class Node {
    int val;
    Node parent;
    Node left;
    Node right;

    public Node(int val) {
        this.val = val;
    }
}