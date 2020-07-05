
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
 
public class Main {
     
    public static class TreeNode {
 
        public int value;
        public TreeNode left;
        public TreeNode right;
 
        public TreeNode(int value) {
            this.value = value;
        }
    }
 
    public static class ReturnType {
 
        public TreeNode start;
        public TreeNode end;
 
        public ReturnType (TreeNode start, TreeNode end) {
            this.start = start;
            this.end = end;
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
     
    public static TreeNode convert(TreeNode root) {
        if (root == null) {
            return null;
        }
        return process(root).start;
    }
 
    private static ReturnType process(TreeNode root) {
        if (root == null) {
            return new ReturnType(null, null);
        }
        ReturnType leftList = process(root.left);
        ReturnType rightList = process(root.right);
        if (leftList.end != null) {
            leftList.end.right = root;
        }
        root.left = leftList.end;
        root.right = rightList.start;
        if (rightList.start != null) {
            rightList.start.left = root;
        }
        return new ReturnType(leftList.start == null ? root : leftList.start,
                rightList.end == null ? root : rightList.end);
    }
 
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bufferedReader.readLine());
        String[][] numbers = new String[n][3];
        for (int i = 0; i < n; i++) {
            numbers[i] = bufferedReader.readLine().split(" ");
        }
        TreeNode root = treeGenerator(n, numbers);
        TreeNode head = convert(root);
        while (head != null) {
            System.out.print(head.value + " ");
            head = head.right;
        }
        
    }
}
