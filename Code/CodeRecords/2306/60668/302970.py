import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Stack;
 
public class Main {
 
    public static class TreeNode {
 
        public int value;
        public TreeNode left;
        public TreeNode right;
 
        public TreeNode(int value) {
            this.value = value;
        }
    }
     
    public static TreeNode treeGenerator(int count, String[][] numbers) {
        HashMap<Integer, TreeNode> map = new HashMap<>();
        map.put(0, null);
        String[] number;
        int value;
        for (int i = 0; i < count; i++) {
            number = numbers[i];
            value = Integer.parseInt(number[0]);
            if (value != 0) {
                map.put(value, new TreeNode(value));
            }
        }
        TreeNode cur;
        for (int i = 0; i < count; i++) {
            number = numbers[i];
            value = Integer.parseInt(number[0]);
            cur = map.get(value);
            cur.left = map.get(Integer.parseInt(number[1]));
            cur.right = map.get(Integer.parseInt(number[2]));
        }
        return map.get(Integer.parseInt(numbers[0][0]));
    }
     
    public static void preOrderRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        System.out.print(root.value + " ");
        preOrderRecur(root.left);
        preOrderRecur(root.right);
    }
 
    public static void inOrderRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        inOrderRecur(root.left);
        System.out.print(root.value + " ");
        inOrderRecur(root.right);
    }
 
    public static void posOrderRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        posOrderRecur(root.left);
        posOrderRecur(root.right);
        System.out.print(root.value + " ");
    }
 
    public static void preOrderUnRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        TreeNode node;
        while (!stack.isEmpty()) {
            node = stack.pop();
            System.out.print(node.value + " ");
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
    }
 
    public static void inOrderUnRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        TreeNode node = root.left;
        while (!stack.isEmpty() || node != null) {
            if (node != null) {
                stack.push(node);
                node = node.left;
            } else {
                node = stack.pop();
                System.out.print(node.value + " ");
                node = node.right;
            }
        }
    }
 
    public static void posOrderUnRecur(TreeNode root) {
        if (root == null) {
            return;
        }
        Stack<TreeNode> stack1 = new Stack<>();
        Stack<TreeNode> stack2 = new Stack<>();
        stack1.push(root);
        TreeNode node;
        while (!stack1.isEmpty()) {
            node = stack1.pop();
            stack2.push(node);
            if (node.left != null) {
                stack1.push(node.left);
            }
            if (node.right != null) {
                stack1.push(node.right);
            }
        }
        while (!stack2.isEmpty()) {
            node = stack2.pop();
            System.out.print(node.value + " ");
        }
    }
     
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bufferedReader.readLine().split(" ")[0]);
        String[][] numbers = new String[n][3];
        for (int i = 0; i < n; i++) {
            numbers[i] = bufferedReader.readLine().split(" ");
        }
        TreeNode root = treeGenerator(n, numbers);
        preOrderUnRecur(root);
        System.out.println();
        inOrderUnRecur(root);
        System.out.println();
        posOrderUnRecur(root);
    }
}