import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
 
public class Main {
     
    static class TreeNode {
 
    public int value;
    public TreeNode left;
    public TreeNode right;
 
    public TreeNode(int value) {
        this.value = value;
    }
    }
     
    private static List<Integer> result = new ArrayList<>();
 
 
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        bf.readLine().split(" ");
        TreeNode root = createTreeCore(bf);
        midRecur(root);
        System.out.println(isSorted(result));
        System.out.println(isCBT(root));
    }
     
        private static boolean isCBT(TreeNode root) {
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        boolean[] flag = new boolean[1];
        queue.offer(root);
 
        while (!queue.isEmpty()) {
            TreeNode treeNode = queue.poll();
            if (treeNode != null) {
                if (flag[0] && !isLeaf(treeNode)) {
                    return false;
                }
                if (treeNode.left == null && treeNode.right != null) {
                    return false;
                }
                if (!flag[0] && treeNode.right == null) {
                    flag[0] = true;
                }
                queue.offer(treeNode.left);
                queue.offer(treeNode.right);
            }
        }
        return true;
    }
 
    private static boolean isLeaf(TreeNode node) {
        return (node.left == null) && (node.right == null);
    }
 
    private static boolean isSorted(List<Integer> list) {
        if (list.size() == 1) {
            return true;
        }
        for (int i = 0; i< list.size() - 1; i++) {
            if (list.get(i) > list.get(i+1)) {
                return false;
            }
        }
        return true;
    }
 
    private static void midRecur(TreeNode treeNode) {
        if (treeNode == null) {
            return ;
        }
        midRecur(treeNode.left);
        result.add(treeNode.value);
        midRecur(treeNode.right);
    }
 
 
    private static TreeNode createTreeCore(BufferedReader in) throws Exception {
        int[] nodes = getIntArray(in.readLine());
        TreeNode treeNode = new TreeNode(nodes[0]);
        if (nodes[1] != 0) {
            treeNode.left = createTreeCore(in);
        }
        if (nodes[2] != 0) {
            treeNode.right = createTreeCore(in);
        }
        return treeNode;
    }
 
    private static int[] getIntArray(String str) {
        String[] temp = str.split(" ");
        int[] result = new int[temp.length];
        for (int i = 0; i < temp.length; i++) {
            result[i] = Integer.parseInt(temp[i]);
        }
        return result;
    }
}