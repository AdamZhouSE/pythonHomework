import java.util.Scanner;
    
   
public class Main {
    static class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
    }
    
    /**
     * 添加一个in作为参数
     * @param in
     * @return
     */
    public static TreeNode createTreeNode(Scanner in){
        int[] nodes=getIntArray(in.nextLine());
        TreeNode node=new TreeNode();
        node.val=nodes[0];
        if(nodes[1]!=0){
            //左孩子
            node.left=createTreeNode(in);
        }
        if(nodes[2]!=0){
            //右孩子
            node.right=createTreeNode(in);
        }
        return node;
    }
    /**
     * 先序遍历
     */
    public static StringBuilder  preOrder(TreeNode treeNode,StringBuilder sb){
     if (treeNode==null){
         return null;
     }
     sb.append(treeNode.val+" ");
     preOrder(treeNode.left,sb);
     preOrder(treeNode.right,sb);
     return sb;
    }
    
     public static StringBuilder innerOrder(TreeNode treeNode,StringBuilder sb){
         if (treeNode==null){
             return null;
         }
         innerOrder(treeNode.left,sb);
         sb.append(treeNode.val);
         sb.append(" ");
         innerOrder(treeNode.right,sb);
         return sb;
    
     }
    
    public static StringBuilder reviewOrder(TreeNode treeNode,StringBuilder sb){
        if (treeNode==null){
            return null;
        }
        reviewOrder(treeNode.left,sb);
        reviewOrder(treeNode.right,sb);
        sb.append(treeNode.val);
        sb.append(" ");
        return sb;
    
    }
     public static int[] getIntArray(String str){
        String[] temp=str.split(" ");
        int[] result=new int[temp.length];
        for(int i=0;i<temp.length;i++){
            result[i]=Integer.parseInt(temp[i]);
        }
        return result;
    }
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        if (in.hasNextLine()) {
            String str = in.nextLine();
        }
        StringBuilder sb =new StringBuilder();
        TreeNode treeNode = createTreeNode(in);
        preOrder(treeNode,sb);
        System.out.print(sb.substring(0, sb.length() - 1));
        sb.delete(0,sb.length()-1);
        sb.append("\n");
        Main.innerOrder(treeNode,sb);
        System.out.print(sb.substring(0, sb.length() - 1));
        sb.delete(0,sb.length()-1);
        sb.append("\n");
        Main.reviewOrder(treeNode,sb);
        System.out.println(sb.substring(0, sb.length() - 1));
    }
}