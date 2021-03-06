
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
 
 
public class Main {
    static int maxLen = 0;
     
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        TreeNode root = createTree(scanner, n);
        int sum = scanner.nextInt();
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 0);
        maxLength(root,sum,map,0,1);
        System.out.println(maxLen);
    }
     
     
     
    private static void maxLength(TreeNode node, int sum, Map<Integer, Integer> map, int preSum, int level) {
        if(node==null) return;
        int currSum = preSum + node.value;
        if(!map.containsKey(currSum)) {
            map.put(currSum, level);
        }
        if(map.containsKey(currSum-sum)) {
            maxLen = Math.max(maxLen, level - map.get(currSum-sum));
        }
        maxLength(node.left,sum,map,currSum,level+1);
        maxLength(node.right,sum,map,currSum,level+1);
        if(map.get(currSum) == level) {
            map.remove(currSum);
        }
    }
 
 
 
    public static TreeNode createTree(Scanner scanner,int n) {
        Map<Integer, TreeNode> map = new HashMap<Integer, TreeNode>();
        int val = scanner.nextInt();
        TreeNode root = new TreeNode();
        map.put(val, root);
        for(int i=0;i<n;i++) {
            int father = scanner.nextInt();
            TreeNode node = map.get(father);
             
            int leftId = scanner.nextInt();
            if(leftId!=0) {
                TreeNode  left = new TreeNode();
                map.put(leftId,left );
                node.left = left;
            }
             
            int rightId = scanner.nextInt();
            if(rightId != 0) {
                TreeNode right = new TreeNode();
                map.put(rightId, right);
                node.right = right;
            }
             
            int value = scanner.nextInt();
            node.value = value;
             
        }
        return root;
    }
}
 
 
class TreeNode{
    int value;
    TreeNode left;
    TreeNode right;
    public TreeNode(int value, TreeNode left, TreeNode right) {
        super();
        this.value = value;
        this.left = left;
        this.right = right;
    }
    public TreeNode(int value) {
        super();
        this.value = value;
        this.left = null;
        this.right = null;
    }
    public TreeNode() {
    }
     
}